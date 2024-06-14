import matplotlib.pyplot as plt
from utils.global_functions import read_coordinates
import re

# Mostrar histograma
def show_histogram(scenario_df, file_number):
    # Calcula la ley de metal de cada cubo
    scenario_df['metal_law_gold'] = scenario_df['gold_tonn'] / scenario_df['total_tonn']
    
    # Crea un histograma
    plt.subplot(2, 1, 1)
    plt.hist(scenario_df['metal_law_gold'], bins=10, edgecolor='black')
    plt.title(f'Histograma de Leyes de Metal: Escenario {file_number}')
    plt.xlabel('Ley de metal')
    plt.ylabel('Frecuencia')
    plt.grid(True)

# Mostrar curva
def show_curve(scenario_df, file_number):
    # Ordena el DataFrame por ley de metal
    scenario_df = scenario_df.sort_values(by='metal_law_gold', ascending=False)
    
    # Reinicia los índices
    scenario_df = scenario_df.reset_index(drop=True)
    
    # Crea una curva de ley de metal
    plt.subplot(2, 1, 2)
    plt.plot(scenario_df.index, scenario_df['metal_law_gold'])
    plt.title(f'Curva de Tonelaje vs Ley de Metal: Escenario {file_number}')
    plt.ylabel('Ley de metal')
    plt.grid(True)

# Mostrar estadísticas de un escenario
def show_scenario_statistics(file_name):
    # Obtiene el número de escenario
    file_number = int(re.search(r'\d+', file_name).group()) + 1
    
    # Lee las coordenadas del archivo
    coordinates_df = read_coordinates(file_name)
    
    # Crea una figura
    plt.figure(figsize=(10, 6))
    
    # Muestra el histograma y la curva
    show_histogram(coordinates_df, file_number)
    show_curve(coordinates_df, file_number)
    
    # Ajusta el diseño
    plt.tight_layout()
    
    # Muestra la figura
    plt.show()
