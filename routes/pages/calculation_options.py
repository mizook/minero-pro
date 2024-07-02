import asyncio

from nicegui import ui

from app.amount_rock import calculate_amount_rock
from routes.constants import calculation_options_path, calculations_path, upl_options
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

# Variables globales
period_value = 1
law_range: dict = {"min": 0, "max": 100}

# Manejar el evento de hacer click en el botón
async def handle_button_click(button, file_name, period, is_upl, output_table, law_range, scenario_num):
    # Agregar estado de carga al botón
    button.props("loading")
    # Si se apretó el botón para calcular UPL
    if is_upl:
        ui.navigate.to(upl_options(scenario_num))
    # Si se apretó el botón para calcular la cantidad de roca en un periodo
    else:
        # Validar que el periodo sea un número entero
        try:
            period = int(period)
        except ValueError:
            button.props(remove="loading")
            return
        # Calcular cantidad de roca en un periodo si el periodo se encuentra en el rango
        if period in range(0,6): 
            results = calculate_amount_rock(file_name, period - 1, law_range)
            global amount_rock, amount_rock_a, amount_rock_b, amount_metal, amount_metal_2
            amount_rock, amount_rock_a, amount_rock_b, amount_metal, amount_metal_2 = results

            # Actualizar la tabla con los nuevos valores
            output_table.rows = [
                {'type': 'Roca general', 'amount': f"{amount_rock:.2f}"},
                {'type': 'Roca A', 'amount': f"{amount_rock_a:.2f}"},
                {'type': 'Roca B', 'amount': f"{amount_rock_b:.2f}"},
                {'type': 'Metal', 'amount': f"{amount_metal:.2f}"},
                {'type': 'Metal 2', 'amount': f"{amount_metal_2:.2f}"},
            ]

    # Remover el estado de carga del botón
    button.props(remove="loading")

# Crear botón para realizar cálculos
def create_button(button_title, scenario_num, is_upl, output_table, law_range):
    file_name = f"Scenario0{scenario_num}.txt"
    button = ui.button(button_title)
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_button_click(button, file_name, period_value, is_upl, output_table, law_range, scenario_num)
        ),
    )
    button.classes(UICommons.statistics_button_class)
    return button

def create_button_upl(scenario_num):
    return ui.button(
        "Ultimate Pit Limit",
        on_click=lambda: ui.navigate.to(upl_options(scenario_num)),
    ).classes(UICommons.statistics_button_class)

# Validar que el valor ingresado sea un número entero
def validate_integer_value(value: str) -> str | None:
    try:
        parsed_value = int(value)
        return validate_integer_range(parsed_value)
    except ValueError:
        return "Debes ingresar un número entero."
    return None

# Validar que el valor ingresado esté en un rango específico
def validate_integer_range(value: int) -> str | None:
    if value < 0 or value > 5:
        return "El valor debe ir de 0 a 5."
    return None

# Actualizar el valor de la variable global
def on_input_value_change(obj: object):
    global period_value
    period_value = obj.value

# Actualizar el rango de ley
def on_ore_grade_range_change(obj: object):
    global law_range
    law_range["min"] = obj.value["min"]
    law_range["max"] = obj.value["max"]

@ui.page(
    f"{calculations_path}/{calculation_options_path}/{{scenery_index}}",
    title="Minero Pro | Opciones de cálculo",
    favicon=utl.get_app_favicon(),
    dark=True,
)

# Página de opciones de cálculo
def calculation_options_page(scenery_index: str = "1"):
    # Crear columnas para la tabla
    columns = [
        {
            'name': 'type', 
            'label': 'Tipo', 
            'field': 'type', 
            'required': True, 
            'align': 'left'
        },
        {
            'name': 'amount', 
            'label': 'Cantidad', 
            'field': 'amount', 
            'sortable': True},
    ]

    # Reiniciar cantidad de roca, metal y segundo metal
    period_value = 0
    amount_rock = 0
    amount_rock_a = 0
    amount_rock_b = 0
    amount_metal = 0
    amount_metal_2 = 0

    # Crear lista de periodos
    periods = [1, 2, 3, 4, 5]

    # Obtener botón para volver atrás
    ui.link("<- Volver atrás", calculations_path).classes("text-yellow-8")

    # Crear elementos de la página
    with ui.element("div").classes("grid place-items-center w-full h-[500px]"):
        # Crear título de la página
        with ui.element("div").classes("inline-flex"):
            ui.label(f"Escenario {int(scenery_index) + 1}").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        # Crear lista de botones
        with ui.list().classes("grid place-items-center h-full w-max-md mt-10"):
            # Crear botón para calcular UPL
            create_button_upl(scenery_index)
            # Título de la sección de calcular la cantidad de roca en un periodo
            ui.label("Cantidad de roca extraída en un periodo").classes("text-2xl mt-3")
            
#           # Crear input para ingresar el periodo
            with ui.grid().classes("w-full place-items-start"):
                ui.label("Filtrar por periodo").classes("text-lg text-left")
            ui.select(periods, value=period_value).classes(
                "w-full"
            ).on_value_change(callback=on_input_value_change)

            # Crear slide para filtrar por rango de ley
            with ui.grid().classes("w-full place-items-start mt-10 mb-5"):
                ui.label("Filtrado por rango de Ley").classes("text-lg text-left")
            min_max_range = ui.range(
                min=law_range['min'], max=law_range['max'], value=law_range
            ).on_value_change(callback=on_ore_grade_range_change)
            ui.label().bind_text_from(
                min_max_range,
                "value",
                backward=lambda v: f'min: {v["min"]}, max: {v["max"]}',
            ).classes("mb-5")

            # Crear las filas de las cantidades de roca y metal a la tabla
            rows = [
                {'type': 'Roca general', 'amount': f"{amount_rock:.2f}"},
                {'type': 'Roca A', 'amount': f"{amount_rock_a:.2f}"},
                {'type': 'Roca B', 'amount': f"{amount_rock_b:.2f}"},
                {'type': 'Metal', 'amount': f"{amount_metal:.2f}"},
                {'type': 'Metal 2', 'amount': f"{amount_metal_2:.2f}"},
            ]

            # Crear tabla para mostrar las cantidades de roca y metal
            output_table = ui.table(rows=rows, columns=columns).classes("w-full")
                        
            # Crear botón para calcular la cantidad de roca en un periodo
            create_button(
                "Calcular",
                int(scenery_index),
                False,
                output_table,
                law_range,
            )

    get_footer()
