from nicegui import ui

from routes.constants import calculations_path, calculation_options
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

# Crear botón para cada escenario
def create_button(scenario_num):
    return ui.button(
        f"Escenario {scenario_num+1}",
        on_click=lambda: ui.navigate.to(
            calculation_options(scenario_num)
        ),
    ).classes(UICommons.statistics_button_class)

@ui.page(
    calculations_path,
    title="Minero Pro | Cálculos",
    favicon=utl.get_app_favicon(),
    dark=True,
)

# Página de cálculos
def calculations_page():
    # Obtener botón para volver atrás
    get_go_back_button()

    # Crear elementos de la página
    with ui.element("div").classes("grid place-items-center w-full h-[500px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("¡Cálculos!").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        # Crear lista de botones
        with ui.list().classes("grid place-items-center grid-cols-2 gap-x-5 mt-10"):
            for index in range(10):
                create_button(index)

    get_footer()
