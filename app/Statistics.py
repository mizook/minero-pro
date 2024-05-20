import matplotlib.pyplot as plt
import pandas as pd

file_name_main = ''

def read_coordinates(filename):
    df = pd.read_csv(f'data/scenarios/{filename}', header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"])
    return df

def show_histogram(scenario_df, file):
    scenario_df['Ley_Metal'] = scenario_df['Metal'] / scenario_df['Tonelaje']

    plt.subplot(2, 1, 1)
    plt.hist(scenario_df['Ley_Metal'], bins=10, edgecolor='black')
    plt.title(f'Histograma de Leyes de Metal: {file}')
    plt.xlabel('Ley de metal')
    plt.ylabel('Frecuencia')
    plt.grid(True)

def show_curve(scenario_df, file):
    scenario_df = scenario_df.sort_values(by='Ley_Metal', ascending=False)

    scenario_df = scenario_df.reset_index(drop=True)

    plt.subplot(2, 1, 2)
    plt.plot(scenario_df['Ley_Metal'])
    plt.title(f'Curva de tonelaje vs ley de metal: {file}')
    plt.ylabel('Ley de metal')
    plt.grid(True)

def show_scenario_statistics(file_name):
    file_name_main = file_name
    coordinates_df = read_coordinates(file_name)

    plt.figure(figsize=(10, 6))

    show_histogram(coordinates_df, file_name)
    show_curve(coordinates_df, file_name)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_scenario_statistics(file_name_main)
