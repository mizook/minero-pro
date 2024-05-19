import tkinter as tk
from tkinter import ttk

import numpy as np
import pyvista as pv


# Define the function to read the file and render the PyVista mesh
def render_mesh():
    # Leer las coordenadas desde el archivo de texto
    file_path = file_entry.get()
    data = np.loadtxt(file_path, delimiter=",", dtype=float)

    # Extraer las coordenadas x, y, z y el tonelaje de cada fila
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    tonelaje = data[:, 3]

    # Crear una malla PyVista a partir de las coordenadas x, y, z
    mesh = pv.StructuredGrid(x, y, z)

    # Agregar el tonelaje como datos escalares a la malla
    mesh["tonelaje"] = tonelaje

    # Deformar la malla según el tonelaje
    warped = mesh.warp_by_scalar()

    # Visualizar la malla deformada como un mapa de elevación superficial con colores según el tonelaje
    p = pv.Plotter()
    p.add_mesh(warped, scalars="tonelaje", cmap="viridis")
    p.show()


# Create the main window
root = tk.Tk()
root.title("PyVista Mesh Renderer")

# Create and pack the widgets
file_label = ttk.Label(root, text="File Path:")
file_label.pack(padx=10, pady=5)

file_entry = ttk.Entry(root, width=40)
file_entry.pack(padx=10, pady=5)

render_button = ttk.Button(root, text="Render Mesh", command=render_mesh)
render_button.pack(padx=10, pady=20)

# Run the GUI event loop
root.mainloop()
