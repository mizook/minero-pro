import multiprocessing
import threading

import pyvista as pv

from app.plot_common import PlotCommon
from utils.utils import Utils as utl


def abstract_rendering(
    file_name: str, ore_grade_range: dict | None = None, rock_type: str | None = None
):
    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = utl.read_coordinates(path)

    grid = PlotCommon.get_deposit_grid(
        coordinates_df, ore_grade_range=ore_grade_range, rock_type=rock_type
    )

    plotter = pv.Plotter()
    return grid, plotter


def rendering_2d(file_name: str, title: str, axis_view: str, event):
    grid, plotter = abstract_rendering(file_name)
    plotter.add_mesh(grid, show_edges=True, pickable=False, label="Vista 2D")
    plotter.show_axes()
    plotter.show_grid()

    if axis_view == "X":
        plotter.view_xy()
    elif axis_view == "Y":
        plotter.view_yz()
    elif axis_view == "Z":
        plotter.view_xz()
    else:
        raise ValueError("Expected axis_view value is X,Y or >")

    plotter.disable()

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()

    event.set()


def rendering_slice_2d(file_name: str, title: str, axis: str, cord: int, event):
    lower_axis = axis.lower()
    if lower_axis not in ["x", "y", "z"]:
        raise ValueError("Expected axis value is x,y or z")

    grid, plotter = abstract_rendering(file_name)
    sliced_mesh = grid.slice(normal=lower_axis)

    plotter.add_mesh(sliced_mesh, show_edges=True)
    plotter.show_axes()
    plotter.show_grid()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def open_2d_scenery(file_name: str, title: str, axis: str, cord: int, event):
    process = multiprocessing.Process(
        target=rendering_slice_2d, args=(file_name, title, axis, cord, event)
    )
    process.start()


def rendering_3d(file_name: str, title: str, event):
    grid, plotter = abstract_rendering(file_name)

    plotter.add_mesh(grid, show_edges=True)
    plotter.show_axes()
    plotter.show_grid()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def rendering_filtered_3d(
    file_name: str, title: str, ore_grade_range: dict, rock_type: str, event: any
):
    grid, plotter = abstract_rendering(
        file_name, ore_grade_range=ore_grade_range, rock_type=rock_type
    )

    plotter.add_mesh(grid, show_edges=True)
    plotter.show_axes()
    plotter.show_grid()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def open_3d_scenery(file_name: str, title: str, event):
    process = multiprocessing.Process(
        target=rendering_3d, args=(file_name, title, event)
    )
    process.start()


def open_3d_filtered_scenery(
    file_name: str, title: str, ore_grade_range: dict, rock_type: str, event: any
):
    process = multiprocessing.Process(
        target=rendering_filtered_3d,
        args=(file_name, title, ore_grade_range, rock_type, event),
    )
    process.start()


def abstract_period_rendering(scenery_num: int):
    path = utl.get_resource_path("data/MinePlan.txt")
    coordinates_df = utl.read_period_coordinates(path)

    grid = PlotCommon.get_period_grid(scenery_num, coordinates_df)

    plotter = pv.Plotter()
    return grid, plotter


def rendering_3d_period(scenery_num: int, title: str, event):
    grid, plotter = abstract_period_rendering(scenery_num)

    plotter.add_mesh(grid, show_edges=True)
    plotter.show_axes()
    plotter.show_grid()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def open_3d_period_scenery(scenery_num: int, title: str, event):
    process = multiprocessing.Process(
        target=rendering_3d_period, args=(scenery_num, title, event)
    )
    process.start()
