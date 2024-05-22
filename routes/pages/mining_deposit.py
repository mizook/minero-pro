from nicegui import ui
from app.PyVistaExample import open_scenery
from routes.constants import mining_deposit_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.utils import Utils as utl

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page(mining_deposit_path, title="Minero Pro | Yacimiento Minero", favicon=utl.get_app_favicon(), dark=True)
def mining_deposit_page():
    get_go_back_button()

    with ui.element('div').classes('grid place-items-center w-full h-[720px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Yacimiento Minero!').classes(title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center mt-10'):
            ui.button('Visualizar Escenario 1', on_click=lambda: open_scenery('Scenario00.txt', "Escenario 1")).classes(
                button_class)
            ui.button('Visualizar Escenario 2', on_click=lambda: open_scenery('Scenario01.txt', "Escenario 2")).classes(
                button_class)
            ui.button('Visualizar Escenario 3', on_click=lambda: open_scenery('Scenario02.txt', "Escenario 3")).classes(
                button_class)
            ui.button('Visualizar Escenario 4', on_click=lambda: open_scenery('Scenario03.txt', "Escenario 4")).classes(
                button_class)
            ui.button('Visualizar Escenario 5', on_click=lambda: open_scenery('Scenario04.txt', "Escenario 5")).classes(
                button_class)
            ui.button('Visualizar Escenario 6', on_click=lambda: open_scenery('Scenario05.txt', "Escenario 6")).classes(
                button_class)
            ui.button('Visualizar Escenario 7', on_click=lambda: open_scenery('Scenario06.txt', "Escenario 7")).classes(
                button_class)
            ui.button('Visualizar Escenario 8', on_click=lambda: open_scenery('Scenario07.txt', "Escenario 8")).classes(
                button_class)
            ui.button('Visualizar Escenario 9', on_click=lambda: open_scenery('Scenario08.txt', "Escenario 9")).classes(
                button_class)
            ui.button('Visualizar Escenario 10',
                      on_click=lambda: open_scenery('Scenario09.txt', "Escenario 10")).classes(button_class)

    get_footer()
