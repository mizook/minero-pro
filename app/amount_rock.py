from utils.utils import Utils as utl

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

    print(coordinates_df)
    print(mineplan_df)
    print(filtered_mineplan_df)
    print(period)

    return 0
    