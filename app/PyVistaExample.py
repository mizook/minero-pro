import pandas as pd
import pyvista as pv
import multiprocessing
from utils.utils import Utils as utl
import time
import pygetwindow as gw


def read_coordinates(filename):
    df = pd.read_csv(
        filename, header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"]
    )
    return df


def bring_window_to_front(window_title):
    time.sleep(2)  # Wait for the window to be created
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        window.activate()


def pyvista_rendering(file_name: str, title: str, event):
    # Lee las coordenadas del archivo
    path = utl.get_resource_path(f"data/scenarios/{file_name}")
    coordinates_df = read_coordinates(path)

    # Crea un contenedor para todos los cubos
    grid = pv.MultiBlock()

    # Itera sobre cada fila en el DataFrame
    for _, row in coordinates_df.iterrows():
        # Obtiene las coordenadas del cubo
        x, y, z = row["X"], row["Y"], row["Z"]

        # Crea el cubo en la posición dada
        cube = pv.Cube(center=(x, y, z), x_length=1, y_length=1, z_length=1)

        # Agrega el cubo al contenedor
        grid.append(cube)

    # Visualiza los cubos
    plotter = pv.Plotter()
    plotter.add_mesh(grid, color="orange", show_edges=True)
    plotter.show_axes()

    plotter.title = title

    # Start a new thread to bring the window to the front
    import threading
    thread = threading.Thread(target=bring_window_to_front, args=(title,))
    thread.start()

    plotter.show(auto_close=False)  # Ensure the plotter stays open

    event.set()  # Señala que la ventana está lista

    plotter.app.exec_()  # Run the PyVista application


def open_scenery(file_name: str, title: str, event):
    # Create and start a new process for PyVista rendering
    process = multiprocessing.Process(target=pyvista_rendering, args=(file_name, title, event))
    process.start()