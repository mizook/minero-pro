import matplotlib.pyplot as plt
from utils.global_functions import read_coordinates
import re

# Mostrar histograma
def show_histogram(ax, scenario_df, file_number):
    # Calcular la ley de metal de cada cubo
    scenario_df['metal_law_gold'] = scenario_df['gold_tonn'] / scenario_df['total_tonn']
    
    # Crear un histograma
    ax.hist(scenario_df['metal_law_gold'], bins=10, edgecolor='black')
    ax.set_title(f'Histograma de Leyes de Metal: Escenario {file_number}')
    ax.set_xlabel('Ley de metal')
    ax.set_ylabel('Frecuencia')
    ax.grid(True)

# Mostrar curva
def show_curve(ax, scenario_df, file_number):
    # Ordenar el DataFrame por ley de metal
    scenario_df = scenario_df.sort_values(by='metal_law_gold', ascending=False)
    
    # Calcular el tonelaje acumulado y la ley media
    scenario_df['cumulative_tonn'] = scenario_df['total_tonn'].cumsum()
    scenario_df['average_metal_law'] = scenario_df['gold_tonn'].cumsum() / scenario_df['cumulative_tonn']
    
    # Reiniciar los índices
    scenario_df = scenario_df.reset_index(drop=True)
    
    # Primer eje Y (izquierdo) - Tonelaje acumulado
    ax.plot(scenario_df['metal_law_gold'], scenario_df['cumulative_tonn'], 'b-', label='Tonelaje acumulado')
    ax.set_xlabel('Ley de corte de oro')
    ax.set_ylabel('Tonelaje acumulado', color='b')
    ax.tick_params(axis='y', labelcolor='b')
    ax.grid(True)
    
    # Segundo eje Y (derecho) - Ley media
    ax2 = ax.twinx()
    ax2.plot(scenario_df['metal_law_gold'], scenario_df['average_metal_law'], 'r-', label='Ley media')
    ax2.set_ylabel('Ley media', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    # Combinar las leyendas de ambos ejes
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, loc='best')
    
    ax.set_title(f'Curva de Tonelaje-Ley: Escenario {file_number}')
    ax.grid(True)

# Mostrar estadísticas de un escenario
def show_scenario_statistics(file_name):
    # Obtener el número de escenario
    file_number = int(re.search(r'\d+', file_name).group()) + 1
    
    # Leer las coordenadas del archivo
    coordinates_df = read_coordinates(file_name)
    
     # Crear una figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), constrained_layout=True)
    
    # Crear el histograma
    show_histogram(ax1, coordinates_df, file_number)
    
    # Crear la curva
    show_curve(ax2, coordinates_df, file_number)
    
    # Mostrar la figura
    plt.show()
