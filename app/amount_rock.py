from utils.utils import Utils as utl

# Función para calcular cantidad de roca en un periodo
def calculate_amount_rock(file_name: str, period: int):
    # Obtener paths de los archivos
    scenario_path = utl.get_resource_path(f"data/scenarios/{file_name}")
    mineplan_path = utl.get_resource_path(f"data/MinePlan.txt")

    # Leer las coordenadas y el plan minero
    coordinates_df = utl.read_coordinates(scenario_path)
    mineplan_df = utl.read_mineplan(mineplan_path)

    return 0