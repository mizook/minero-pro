from nicegui import ui

from routes.constants import deposit_options, mining_deposit_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


def create_button(scenario_num):
    return ui.button(
        f"Escenario {int(scenario_num) + 1}",
        on_click=lambda: ui.navigate.to(deposit_options(scenario_num)),
    ).classes(UICommons.statistics_button_class)


@ui.page(
    mining_deposit_path,
    title="Minero Pro | Yacimiento Minero",
    favicon=utl.get_app_favicon(),
    dark=True,
)
def mining_deposit_page():
    get_go_back_button()

    with ui.element("div").classes("grid place-items-center w-full h-[500px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("¡Yacimiento Minero!").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center grid-cols-2 gap-x-5 mt-10"):
            for index in range(10):
                create_button(index)

    get_footer()
