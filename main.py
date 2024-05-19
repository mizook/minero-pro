import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

HEADERS = ["X", "Y", "Z", "TONELAJE", "METAL", "METAL 2"]


def read_scenarios():
    scenarios_list = []
    for file in os.listdir('scenarios'):
        scenarios_list.append(file)
    return scenarios_list


def block_colors(scenario_df):
    # Encontrar el valor máximo y mínimo de la columna "METAL"
    max_metal = scenario_df['METAL'].max()
    min_metal = scenario_df['METAL'].min()

    # Calcular el promedio ponderado
    weighted_average = (max_metal + min_metal) / 2

    # Definir colores para el degradado
    colors = ['#8B4513', '#D2B48C']  # Tierra a color de roca (gris claro)

    # Calcular la dispersión de los valores de "METAL"
    dispersion = max_metal - min_metal

    # Calcular los valores normalizados de "METAL"
    normalized_metal = (scenario_df['METAL'] - min_metal) / dispersion

    # Asignar colores basados en los valores normalizados
    custom_colors = []
    for val in normalized_metal:
        custom_colors.append(colors[int(round(val))])
    return custom_colors


def main():
    files_list = read_scenarios()
    scenario_df = pd.read_csv(f'scenarios/{files_list[0]}', sep=',')

    scenario_df.columns = HEADERS

    # Coordenadas para los bloques
    x = scenario_df['X']
    y = scenario_df['Y']
    z = scenario_df['Z']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Tamaño de los bloques
    dx = np.ones_like(x)
    dy = np.ones_like(y)
    dz = np.ones_like(z)

    # Plot de los bloques
    ax.bar3d(x, y, z, dx, dy, dz, color=block_colors(scenario_df))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


if __name__ == "__main__":
    main()
