import pyvista as pv
import numpy as np

# Leer las coordenadas desde el archivo de texto
file_path = 'scenarios/Scenario00.txt'
data = np.loadtxt(file_path, delimiter=',', dtype=float)

# Extraer las coordenadas x, y, z y el tonelaje de cada fila
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
tonelaje = data[:, 3]

# Crear una malla PyVista a partir de las coordenadas x, y, z
mesh = pv.StructuredGrid(x, y, z)

# Agregar el tonelaje como datos escalares a la malla
mesh['tonelaje'] = tonelaje

# Deformar la malla según el tonelaje
warped = mesh.warp_by_scalar()

# Visualizar la malla deformada como un mapa de elevación superficial con colores según el tonelaje
p = pv.Plotter()
p.add_mesh(warped, scalars='tonelaje', cmap='viridis')
p.show()
