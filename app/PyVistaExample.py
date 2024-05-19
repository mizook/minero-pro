import pandas as pd
import pyvista as pv

def read_coordinates(filename):
    df = pd.read_csv(filename, header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"])
    return df

def open_scenary(file_name):
    # Lee las coordenadas del archivo
    coordinates_df = read_coordinates("data/scenarios/Scenario09.txt")

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
    plotter.show()

if __name__ == "__main__":
    open_scenary('Scenario00.txt')