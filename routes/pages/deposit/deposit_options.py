from nicegui import ui

from app.modeler import open_3d_scenery, open_2d_scenery
from routes.constants import mining_deposit_path, deposit_path
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl
import asyncio
import multiprocessing


async def handle_button_click(button, file_name, title, is_2d):
    button.set_text("Cargando...")
    button.props('loading')
    event = multiprocessing.Event()
    process = multiprocessing.Process(target=open_2d_scenery if is_2d else open_3d_scenery,
                                      args=(file_name, title, event))
    process.start()
    await asyncio.to_thread(event.wait)
    button.set_text(f'Visualizar {title}')
    button.props(remove='loading')


def create_button(button_title: str, scenario_num: str, is_2d: bool = True):
    file_name = f'Scenario0{scenario_num}.txt'
    title = f'Escenario {scenario_num}'
    button = ui.button(button_title)
    button.on('click', lambda _: asyncio.create_task(handle_button_click(button, file_name, title, is_2d)))
    button.classes(UICommons.button_class)
    return button


@ui.page(f"{deposit_path}/{{scenery_index}}", title="Minero Pro | AAA", favicon=utl.get_app_favicon(), dark=True)
def deposit_options_page(scenery_index: str = "1"):
    ui.link('<- Volver atrás', mining_deposit_path).classes('text-yellow-8')
    with ui.element('div').classes('grid place-items-center w-full h-[550px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label(f'Scenario {scenery_index}').classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center w-full h-full'):
            create_button("Visualización 3D", scenery_index, is_2d=False)
            create_button("Visualización 2D - Eje X", scenery_index)
            create_button("Visualización 2D - Eje Y", scenery_index)
            create_button("Visualización 2D - Eje Z", scenery_index)

    get_footer()
