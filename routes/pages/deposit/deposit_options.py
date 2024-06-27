import asyncio
import multiprocessing

from nicegui import ui

from app.modeler import open_2d_scenery, open_3d_scenery
from routes.constants import deposit_path, mining_deposit_path
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


async def handle_button_click(button, file_name, title, axis_view, is_2d):
    if is_2d and axis_view not in ["X", "Y", "Z"]:
        raise ValueError("axis_view should be X, Y or Z when 2D view is enabled")
    button.props("loading")
    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target=open_2d_scenery if is_2d else open_3d_scenery,
        args=(file_name, title, axis_view, event)
        if is_2d
        else (file_name, title, event),
    )
    process.start()
    await asyncio.to_thread(event.wait)
    button.props(remove="loading")


def create_button(
    button_title: str, scenario_num: str, axis_view: str = "", is_2d: bool = True
):
    file_name = f"Scenario0{scenario_num}.txt"
    title = f"Escenario {scenario_num}"
    button = ui.button(button_title)
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_button_click(button, file_name, title, axis_view, is_2d)
        ),
    )
    button.classes(UICommons.button_class)
    return button


@ui.page(
    f"{deposit_path}/{{scenery_index}}",
    title="Minero Pro | AAA",
    favicon=utl.get_app_favicon(),
    dark=True,
)
def deposit_options_page(scenery_index: str = "1"):
    ui.link("<- Volver atrás", mining_deposit_path).classes("text-yellow-8")
    with ui.element("div").classes("grid place-items-center w-full h-[550px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label(f"Scenario {scenery_index}").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center w-full h-full"):
            create_button("Visualización 3D", scenery_index, is_2d=False)
            create_button(
                "Visualización 2D - Eje X", scenery_index, is_2d=True, axis_view="X"
            )
            create_button(
                "Visualización 2D - Eje Y", scenery_index, is_2d=True, axis_view="Y"
            )
            create_button(
                "Visualización 2D - Eje Z", scenery_index, is_2d=True, axis_view="Z"
            )

    get_footer()
