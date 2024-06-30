import asyncio

from nicegui import ui

from app.statistics import show_scenario_statistics
from routes.constants import statistics_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

# 
async def handle_button_click(button, file_name):
    button.props("loading")
    show_scenario_statistics(file_name)
    button.props(remove="loading")

# 
def create_button(button_tittle, scenario_num):
    file_name = f"Scenario0{scenario_num}.txt"
    button = ui.button(button_tittle)
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_button_click(button, file_name)
        ),
    )
    button.classes(UICommons.statistics_button_class)
    return button

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
            for index in range(10):
                create_button(f"Escenario {index + 1}", index)

    get_footer()
