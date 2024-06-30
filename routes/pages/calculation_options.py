from nicegui import ui

from routes.constants import calculation_options_path, calculations_path
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

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

            # Crear botón para calcular cantidad de roca en un periodo
            ui.label("Cantidad de roca en un periodo").classes("text-2xl")
            # Crear input para ingresar el periodo
            ui.input(
                "Periodo",
                validation=True,
                value=True,
            ).classes("w-full").on_value_change(callback=True)
            ui.button(
                "Calcular", 
                on_click=lambda: ui.navigate.to()
            ).classes(UICommons.button_class)

    get_footer()
