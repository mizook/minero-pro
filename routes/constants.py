mining_deposit_path = "/yacimiento-minero"
mining_plan_path = "/plan-minero"
calculations_path = "/calculos"
calculation_options_path = "/opciones-calculos"
statistics_path = "/estadisticas"
home_path = "/"
deposit_path = "/scenery"
plan_path = "/plan"



def deposit_options(scenery_index):
    return f"{deposit_path}/{scenery_index}"


# Crear dirección para las opciones de cálculo
def calculation_options(scenery_index):
    return f"{calculations_path}/{calculation_options_path}/{scenery_index}"


def plan_options(scenery_index):
    return f"{plan_path}/{scenery_index}"
