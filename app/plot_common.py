import time

import numpy as np
import pygetwindow as gw
import pyvista as pv

from utils.utils import Utils as utl


class PlotCommon:
    @staticmethod
    def get_deposit_grid(
        coordinates_df,
        ore_grade_range: dict | None = None,
        rock_type: str | None = None,
    ):
        grid = pv.MultiBlock()

        for _, row in coordinates_df.iterrows():
            x, y, z, total_tons, metal_tons, metal_grade = (
                PlotCommon.get_initial_values(row)
            )
            rock_type_flag = PlotCommon.get_rock_type_flag(x, y, rock_type)
            ore_grade_flag = PlotCommon.get_ore_grade_range_flag(
                ore_grade_range, metal_grade
            )

            if rock_type_flag or ore_grade_flag:
                continue

            cube = pv.Cube(center=(x, y, z), x_length=1, y_length=1, z_length=1)

            rgb_value = int(metal_grade)
            rgb_array = np.array([rgb_value, rgb_value, rgb_value], dtype=np.uint8)

            cube["Ley del Mineral"] = np.tile(rgb_array, (cube.n_cells, 1))

            cube.cell_data["Ley del Mineral"] = np.tile(rgb_array, (cube.n_cells, 1))

            grid.append(cube)
        return grid

    @staticmethod
    def get_initial_values(row):
        x, y, z = int(row["X"]), int(row["Y"]), int(row["Z"])
        total_tons = int(row["Tonelaje"])
        metal_tons = int(row["Metal"])
        metal_grade = 0
        if total_tons != 0:
            metal_grade = float((metal_tons / total_tons)) * 100
        return x, y, z, total_tons, metal_tons, metal_grade

    @staticmethod
    def get_rock_type_flag(x_index: int, y_index: int, expected_rock_type: str | None):
        if expected_rock_type is None:
            return False

        if expected_rock_type == "A & B":  # Allow to show both rock types
            return False
        current_rock_type = utl.get_rock_type(x_index, y_index)
        if current_rock_type != expected_rock_type:
            return True  # continue flag to avoid add to mesh
        else:
            # If the rock type matchs, should be added
            return False

    @staticmethod
    def get_ore_grade_range_flag(
        ore_grade_range: dict | None, current_metal_grade: float
    ):
        if ore_grade_range is None:
            return False

        expected_min_value = ore_grade_range["min"]
        expected_max_value = ore_grade_range["max"]
        # If the current metal grade/ore is in range, should be added
        if expected_min_value <= current_metal_grade <= expected_max_value:
            return False
        # Otherwise, should be skipped
        else:
            return True

    @staticmethod
    def bring_window_to_front(window_title):
        time.sleep(2)
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            window.activate()
