import asyncio
import multiprocessing

from nicegui import ui

from app.modeler import open_3d_period_scenery
from routes.constants import mining_plan_path, plan_options
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


def create_button(scenery_num: str):

    parsed_scenery_num = int(scenery_num)

    return ui.button(
        f"Periodo {parsed_scenery_num + 1}",
        on_click=lambda: ui.navigate.to(plan_options(parsed_scenery_num)),
    ).classes(UICommons.statistics_button_class)





@ui.page(
    mining_plan_path,
    title="Minero Pro | Plan Minero",
    favicon=utl.get_app_favicon(),
    dark=True,
)
def mining_plan_page():
    get_go_back_button()

    with ui.element("div").classes("grid place-items-center w-full h-[300px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("¡Plan Minero!").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center grid-cols-2 gap-5 mt-10"):
            for index in range(5):
                create_button(index)

    get_footer()
