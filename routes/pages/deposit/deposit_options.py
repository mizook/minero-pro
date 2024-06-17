from nicegui import ui

from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl
import asyncio
import multiprocessing
from app.PyVistaExample import open_scenery


async def handle_button_click(button, file_name, title):
    button.set_text("Cargando...")
    button.props('loading')
    event = multiprocessing.Event()
    process = multiprocessing.Process(target=open_scenery, args=(file_name, title, event))
    process.start()
    await asyncio.to_thread(event.wait)
    button.set_text(f'Visualizar {title}')
    button.props(remove='loading')


def create_button(scenario_num):
    file_name = f'Scenario0{scenario_num - 1}.txt'
    title = f'Escenario {scenario_num}'
    button = ui.button(f'Visualizar Escenario {scenario_num}')
    button.on('click', lambda _: asyncio.create_task(handle_button_click(button, file_name, title)))
    button.classes(UICommons.statistics_button_class)
    return button


@ui.page("/scenery/{scenery_index}", title="Minero Pro | AAA", favicon=utl.get_app_favicon(), dark=True)
def deposit_options_page(scenery_index: str = "1"):
    with ui.element('div').classes('grid place-items-center w-full h-[550px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label(f'Scenario {scenery_index}').classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center w-full h-full'):
            ui.button('BOTÓN DE PRUEBA', on_click=lambda: ui.navigate.to("/")).classes(
                UICommons.button_class)

    get_footer()
