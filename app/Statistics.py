import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_name_main = ''

def read_coordinates(filename):
    df = pd.read_csv(f'data/scenarios/{filename}', header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"])
    return df

def show_histogram(scenario_df, file):
    scenario_df['Ley_Metal'] = scenario_df['Metal'] / scenario_df['Tonelaje']

    plt.figure(figsize=(10, 6))
    plt.hist(scenario_df['Ley_Metal'], bins=10, edgecolor='black')
    plt.title(f'Histograma de Leyes de Metal: {file}')
    plt.xlabel('Ley de metal')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

def show_curve(scenario_df, file):
    scenario_sorted = scenario_df.sort_values(by='Ley_Metal')

    plt.figure(figsize=(10, 6))
    plt.plot(scenario_sorted['Ley_Metal'], scenario_sorted['Tonelaje'], marker='o')
    plt.title(f'Curva de tonelaje vs ley de metal: {file}')
    plt.xlabel('Ley de metal')
    plt.ylabel('Tonelaje')
    plt.grid(True)
    plt.show()

def show_scenario_statistics(file_name):
    file_name_main = file_name
    coordinates_df = read_coordinates(file_name)
    show_histogram(coordinates_df, file_name)
    show_curve(coordinates_df, file_name)

if __name__ == "__main__":
    show_scenario_statistics(file_name_main)
