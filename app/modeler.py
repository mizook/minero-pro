import pyvista as pv
import multiprocessing

from app.plot_common import PlotCommon
from utils.utils import Utils as utl
import threading


def abstract_rendering(file_name: str):
    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = utl.read_coordinates(path)

    grid = PlotCommon.get_deposit_grid(coordinates_df)

    plotter = pv.Plotter()
    return grid, plotter


def rendering_2d(file_name: str, title: str, event):
    grid, plotter = abstract_rendering(file_name)
    plotter.add_mesh(grid, color="orange", show_edges=True, pickable=False, label="XY View")
    plotter.show_axes()

    plotter.view_xy()
    plotter.disable()

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()

    event.set()


def open_2d_scenery(file_name: str, title: str, event):
    process = multiprocessing.Process(target=rendering_2d, args=(file_name, title, event))
    process.start()


def rendering_3d(file_name: str, title: str, event):
    grid, plotter = abstract_rendering(file_name)
    
    plotter.add_mesh(grid, color="orange", show_edges=True)
    plotter.show_axes()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def open_3d_scenery(file_name: str, title: str, event):
    process = multiprocessing.Process(target=rendering_3d, args=(file_name, title, event))
    process.start()
