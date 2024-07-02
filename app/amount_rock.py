from utils.utils import Utils as utl

# Función para sumar la cantidad de roca
def sum_amount_rock(mineplan_df, coordinates_df, law_range):
    amount_rock = 0
    amount_rock_a = 0
    amount_rock_b = 0
    amount_metal = 0
    amount_metal_2 = 0

    # Iterar sobre el plan minero y sumar la cantidad de roca
    for _, row in mineplan_df.iterrows():
        # Obtener las coordenadas del plan minero
        x_index, y_index, z_index = row["XIndex"], row["YIndex"], row["ZIndex"]
        # Filtrar el DataFrame de coordenas por las coordenadas del plan minero
        filter_df = (coordinates_df["X"] == x_index) & (coordinates_df["Y"] == y_index) & (coordinates_df["Z"] == z_index)

        # Si existe la coordenada y se encuentra en el rango, sumar cantidad de roca
        if not coordinates_df[filter_df].empty:
            # Calcular la ley de metal
            metal_law = (coordinates_df[filter_df]["Metal"].values[0] / coordinates_df[filter_df]["Tonelaje"].values[0]) * 100
            # Si la ley de metal se encuentra en el rango, sumar cantidad de roca
            if validate_metal_law(metal_law, law_range):
                amount_rock += coordinates_df[filter_df]["Tonelaje"].values[0]
                amount_metal += coordinates_df[filter_df]["Metal"].values[0]
                amount_metal_2 += coordinates_df[filter_df]["Metal2"].values[0]
        # Si no existe la coordenada pero si se encuentra en el rango, sumar cantidad de roca
        else:
            if validate_metal_law(0, law_range): amount_rock += 15375

        # Si la roca es de tipo A o B y se encuentra en el rango, sumar cantidad de roca
        if utl.get_rock_type(x_index, z_index) == "A" and validate_metal_law(0, law_range):
            amount_rock_a += 15375
        elif utl.get_rock_type(x_index, z_index) == "B"  and validate_metal_law(0, law_range):
            amount_rock_b += 15375

    return (amount_rock, amount_rock_a, amount_rock_b, amount_metal, amount_metal_2)

# Verificar que la ley de metal se encuentre en el rango
def validate_metal_law(metal_law: int, law_range: dict):
    return metal_law >= law_range["min"] and metal_law <= law_range["max"]

# Función para calcular cantidad de roca en un periodo
def calculate_amount_rock(file_name: str = "1", period: int = 0, law_range: dict = {"min": 0, "max": 100}):
    # Obtener paths de los archivos
    scenario_path = utl.get_resource_path(f"data/scenarios/{file_name}")
    mineplan_path = utl.get_resource_path(f"data/MinePlan.txt")

    # Leer las coordenadas y el plan minero
    coordinates_df = utl.read_coordinates(scenario_path)
    mineplan_df = utl.get_mineplan(mineplan_path)

    # Filtrar el plan minero por periodo
    filtered_mineplan_df = mineplan_df[mineplan_df["Period"] == period]

    # Calcular la cantidad de roca en un periodo
    amount_rock, amount_rock_a, amount_rock_b, amount_metal, amount_metal_2 = sum_amount_rock(filtered_mineplan_df, coordinates_df, law_range)

    return (amount_rock, amount_rock_a, amount_rock_b, amount_metal, amount_metal_2)
    