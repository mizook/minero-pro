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

            # Assign a random color for demonstration purposes
            # Replace this with your specific logic for assigning colors
            color = np.random.rand(3)

            # Add the color to the cube
            cube["colors"] = np.tile(color, (cube.n_cells, 1))

            # Set the color mode to cell data
            cube.cell_data["colors"] = np.tile(color, (cube.n_cells, 1))

            grid.append(cube)
        return grid

    @staticmethod
    def bring_window_to_front(window_title):
        time.sleep(2)
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            window.activate()
