import matplotlib.pyplot as plt
from utils.global_functions import read_coordinates
import re


def show_histogram(scenario_df, file_number):
    scenario_df['metal_law_gold'] = scenario_df['gold_tonn'] / scenario_df['total_tonn']
    plt.subplot(2, 1, 1)
    plt.hist(scenario_df['metal_law_gold'], bins=10, edgecolor='black')
    plt.title(f'Histograma de Leyes de Metal: Escenario {file_number}')
    plt.xlabel('Ley de metal')
    plt.ylabel('Frecuencia')
    plt.grid(True)


def show_curve(scenario_df, file_number):
    scenario_df = scenario_df.sort_values(by='metal_law_gold', ascending=False)
    scenario_df = scenario_df.reset_index(drop=True)
    plt.subplot(2, 1, 2)
    plt.plot(scenario_df.index, scenario_df['metal_law_gold'])
    plt.title(f'Curva de Tonelaje vs Ley de Metal: Escenario {file_number}')
    plt.ylabel('Ley de metal')
    plt.grid(True)


def show_scenario_statistics(file_name):
    file_number = int(re.search(r'\d+', file_name).group()) + 1
    coordinates_df = read_coordinates(file_name)
    plt.figure(figsize=(10, 6))
    show_histogram(coordinates_df, file_number)
    show_curve(coordinates_df, file_number)
    plt.tight_layout()
    plt.show()
