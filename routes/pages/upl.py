import asyncio
import multiprocessing

from nicegui import ui

from app.upl_modeler import calculate_upl
from app.modeler import open_3d_pit_scenery
from routes.constants import calculations_path, calculation_options_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.ui_commons import UICommons
from utils.utils import Utils as utl


async def handle_button_click(button, pit_df):
    button.props("loading")

    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target= open_3d_pit_scenery ,
        args=(pit_df, "Ultimate Pit Limit", event),
    )
    process.start()
    await asyncio.to_thread(event.wait)
    button.props(remove="loading")


def create_button(pit_df):
    title = "Visualizar Yacimiento"
    button = ui.button(title)
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_button_click(button, pit_df)
        ),
    )
    button.classes(UICommons.visualization_button_class)
    return button

@ui.page(
    f"{calculations_path}/{calculation_options_path}/{{scenery_index}}/upl",
    title="Minero Pro | Cálculos",
    favicon=utl.get_app_favicon(),
    dark=True,
)

def upl_page(scenery_index: str = '1'):
    file_name = f"Scenario0{scenery_index}.txt"
    
    pit_df, pit_value = calculate_upl(file_name)

    pit_value_formatted = f"{pit_value:,.2f}"
    # Obtener botón para volver atrás
    ui.link("<- Volver atrás", f"{calculations_path}/{calculation_options_path}/{scenery_index}").classes("text-yellow-8")

    # Crear elementos de la página
    with ui.element("div").classes("grid place-items-center w-full h-[500px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label("Ultimate Pit Limit").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        # Crear lista de botones
        with ui.list().classes("grid place-items-center grid-cols-1 gap-x-5 mt-10"):
            ui.label(f"Beneficio total: USD ${pit_value_formatted}").classes(UICommons.title_class).classes("m-5")
            create_button(pit_df)
            

    get_footer()
