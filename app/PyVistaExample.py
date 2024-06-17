import pyvista as pv
import multiprocessing
from utils.utils import Utils as utl
import threading
from app.plot_common import PlotCommon


def pyvista_rendering(file_name: str, title: str, event):
    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = utl.read_coordinates(path)

    grid = PlotCommon.get_deposit_grid(coordinates_df)

    plotter = pv.Plotter()
    plotter.add_mesh(grid, color="orange", show_edges=True)
    plotter.show_axes()

    plotter.title = title

    thread = threading.Thread(target=PlotCommon.bring_window_to_front, args=(title,))
    thread.start()

    plotter.show()
    event.set()


def open_scenery(file_name: str, title: str, event):
    process = multiprocessing.Process(target=pyvista_rendering, args=(file_name, title, event))
    process.start()
