from nicegui import ui
from app.PyVistaExample import open_scenery
from routes.footer import get_footer

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page('/yacimiento-minero', title="Minero Pro | Yacimiento Minero", favicon="assets/minero-pro.svg", dark=True)
def yacimiento_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')

    with ui.element('div').classes('grid place-items-center w-full h-[720px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Yacimiento Minero!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center mt-10'):
            ui.button('Visualizar Escenario 1', on_click=lambda: open_scenery('Scenario00.txt')).classes(button_class)
            ui.button('Visualizar Escenario 2', on_click=lambda: open_scenery('Scenario01.txt')).classes(button_class)
            ui.button('Visualizar Escenario 3', on_click=lambda: open_scenery('Scenario02.txt')).classes(button_class)
            ui.button('Visualizar Escenario 4', on_click=lambda: open_scenery('Scenario03.txt')).classes(button_class)
            ui.button('Visualizar Escenario 5', on_click=lambda: open_scenery('Scenario04.txt')).classes(button_class)
            ui.button('Visualizar Escenario 6', on_click=lambda: open_scenery('Scenario05.txt')).classes(button_class)
            ui.button('Visualizar Escenario 7', on_click=lambda: open_scenery('Scenario06.txt')).classes(button_class)
            ui.button('Visualizar Escenario 8', on_click=lambda: open_scenery('Scenario07.txt')).classes(button_class)
            ui.button('Visualizar Escenario 9', on_click=lambda: open_scenery('Scenario08.txt')).classes(button_class)
            ui.button('Visualizar Escenario 10', on_click=lambda: open_scenery('Scenario09.txt')).classes(button_class)

    get_footer()
