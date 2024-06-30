from utils.utils import Utils as utl

# Función para sumar la cantidad de roca
def sum_amount_rock(mineplan_df, coordinates_df):
    amount_rock = 0
    amount_metal = 0
    amount_metal_2 = 0

    # Iterar sobre el plan minero y sumar la cantidad de roca
    for _, row in mineplan_df.iterrows():
        # Obtener las coordenadas del plan minero
        x_index, y_index, z_index = row["XIndex"], row["YIndex"], row["ZIndex"]
        # Filtrar el DataFrame de coordenas por las coordenadas del plan minero
        filter_df = (coordinates_df["X"] == x_index) & (coordinates_df["Y"] == y_index) & (coordinates_df["Z"] == z_index)
        # Si existe la coordenada, sumar cantidad de roca
        if not coordinates_df[filter_df].empty:
            amount_rock += coordinates_df[filter_df]["Tonelaje"].values[0]
            amount_metal += coordinates_df[filter_df]["Metal"].values[0]
            amount_metal_2 += coordinates_df[filter_df]["Metal2"].values[0]
        # Si no existe la coordenada, sumar cantidad de roca
        else :
            amount_rock += 15375

    return (amount_rock, amount_metal, amount_metal_2)

# Función para calcular cantidad de roca en un periodo
def calculate_amount_rock(file_name: str = "1", period: int = 0):
    # Obtener paths de los archivos
    scenario_path = utl.get_resource_path(f"data/scenarios/{file_name}")
    mineplan_path = utl.get_resource_path(f"data/MinePlan.txt")

    # Leer las coordenadas y el plan minero
    coordinates_df = utl.read_coordinates(scenario_path)
    mineplan_df = utl.get_mineplan(mineplan_path)

    # Filtrar el plan minero por periodo
    filtered_mineplan_df = mineplan_df[mineplan_df["Period"] == period]

    # Calcular la cantidad de roca en un periodo
    amount_rock, amount_metal, amount_metal_2 = sum_amount_rock(filtered_mineplan_df, coordinates_df)

    return (amount_rock, amount_metal, amount_metal_2)
    