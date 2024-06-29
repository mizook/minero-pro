import time

import numpy as np
import pygetwindow as gw
import pyvista as pv


class PlotCommon:
    @staticmethod
    def get_deposit_grid(coordinates_df):
        grid = pv.MultiBlock()

        for _, row in coordinates_df.iterrows():
            x, y, z = row["X"], row["Y"], row["Z"]

            cube = pv.Cube(center=(x, y, z), x_length=1, y_length=1, z_length=1)
            total_tons = row["Tonelaje"]
            metal_tons = row["Metal"]
            metal_grade = 0
            if total_tons != 0:
                metal_grade = float((metal_tons / total_tons)) * 100
            rgb_value = int(metal_grade)
            rgb_array = np.array([rgb_value, rgb_value, rgb_value], dtype=np.uint8)

            cube["Ley del Mineral"] = np.tile(rgb_array, (cube.n_cells, 1))

            cube.cell_data["Ley del Mineral"] = np.tile(rgb_array, (cube.n_cells, 1))

            grid.append(cube)
        return grid

    @staticmethod
    def bring_window_to_front(window_title):
        time.sleep(2)
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            window.activate()
