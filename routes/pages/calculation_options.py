from nicegui import ui

from routes.constants import calculation_options_path, calculations_path
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

# Variables globales
global_cord_value = 0

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
    global global_cord_value
    global_cord_value = obj.value

@ui.page(
    f"{calculations_path}/{calculation_options_path}/{{scenery_index}}",
    title="Minero Pro | Opciones de cálculo",
    favicon=utl.get_app_favicon(),
    dark=True,
)

# Página de opciones de cálculo
def calculation_options_page(scenery_index: str = "1"):
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
            ui.button(
                "Ultimate Pit Limit",
                on_click=lambda: ui.navigate.to(),
            ).classes(UICommons.button_class)

            # Título de la sección de calcular la cantidad de roca en un periodo
            ui.label("Cantidad de roca extraída en un periodo").classes("text-2xl")
            
            # Crear input para ingresar el periodo
            ui.input(
                "Periodo",
                validation=validate_integer_value,
                value=global_cord_value,
            ).classes("w-full").on_value_change(callback=on_input_value_change)
            
            # Crear botón para calcular la cantidad de roca en un periodo
            ui.button(
                "Calcular", 
                on_click=lambda: ui.navigate.to()
            ).classes(UICommons.button_class)

    get_footer()
