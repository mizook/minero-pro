from nicegui import ui

from routes.constants import (
    calculations_path,
    home_path,
    mining_deposit_path,
    mining_plan_path,
    statistics_path,
)
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


@ui.page(
    home_path, title="Minero Pro | Inicio", favicon=utl.get_app_favicon(), dark=True
)
def home_page():
    with ui.element("div").classes("grid place-items-center w-full h-[550px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("¡Bienvenido a Minero Pro!").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center w-full h-full"):
            ui.button(
                "Yacimiento Minero",
                on_click=lambda: ui.navigate.to(mining_deposit_path),
            ).classes(UICommons.button_class)
            ui.button(
                "Plan Minero", on_click=lambda: ui.navigate.to(mining_plan_path)
            ).classes(UICommons.button_class)
            ui.button(
                "Estadísticas", on_click=lambda: ui.navigate.to(statistics_path)
            ).classes(UICommons.button_class)
            ui.button(
                "Cálculos", on_click=lambda: ui.navigate.to(calculations_path)
            ).classes(UICommons.button_class)

    get_footer()
