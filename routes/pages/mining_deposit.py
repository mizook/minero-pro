from nicegui import ui
from app.PyVistaExample import open_scenery
from routes.constants import mining_deposit_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.utils import Utils as utl
import asyncio
import multiprocessing

button_class = 'text-xl font-bold w-[300px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


async def handle_button_click(button, file_name, title):
    button.set_text("Cargando...")
    button.props('loading')
    event = multiprocessing.Event()
    process = multiprocessing.Process(target=open_scenery, args=(file_name, title, event))
    process.start()
    await asyncio.to_thread(event.wait)  # Espera a que el evento sea señalado
    button.set_text(f'Visualizar {title}')
    button.props(remove='loading')


def create_button(scenario_num):
    file_name = f'Scenario0{scenario_num - 1}.txt'
    title = f'Escenario {scenario_num}'
    button = ui.button(f'Visualizar Escenario {scenario_num}')
    button.on('click', lambda _: asyncio.create_task(handle_button_click(button, file_name, title)))
    button.classes(button_class)
    return button


@ui.page(mining_deposit_path, title="Minero Pro | Yacimiento Minero", favicon=utl.get_app_favicon(), dark=True)
def mining_deposit_page():
    get_go_back_button()

    with ui.element('div').classes('grid place-items-center w-full h-[500px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Yacimiento Minero!').classes(title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center grid-cols-2 gap-x-5 mt-10'):
            for i in range(1, 11):
                create_button(i)

    get_footer()