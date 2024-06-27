from nicegui import ui

from app.statistics import show_scenario_statistics
from routes.constants import statistics_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


@ui.page(
    statistics_path,
    title="Minero Pro | Estadísticas",
    favicon=utl.get_app_favicon(),
    dark=True,
)
def statistics_page():
    get_go_back_button()

    with ui.element("div").classes("grid place-items-center w-full h-[500px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("¡Estadísticas!").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center grid-cols-2 gap-x-5 mt-10"):
            ui.button(
                "Escenario 1",
                on_click=lambda: show_scenario_statistics("Scenario00.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 2",
                on_click=lambda: show_scenario_statistics("Scenario01.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 3",
                on_click=lambda: show_scenario_statistics("Scenario02.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 4",
                on_click=lambda: show_scenario_statistics("Scenario03.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 5",
                on_click=lambda: show_scenario_statistics("Scenario04.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 6",
                on_click=lambda: show_scenario_statistics("Scenario05.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 7",
                on_click=lambda: show_scenario_statistics("Scenario06.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 8",
                on_click=lambda: show_scenario_statistics("Scenario07.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 9",
                on_click=lambda: show_scenario_statistics("Scenario08.txt"),
            ).classes(UICommons.statistics_button_class)
            ui.button(
                "Escenario 10",
                on_click=lambda: show_scenario_statistics("Scenario09.txt"),
            ).classes(UICommons.statistics_button_class)

    get_footer()
