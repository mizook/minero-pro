from nicegui import ui
from app.Statistics import show_scenario_statistics
from routes.footer import get_footer

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page('/estadisticas', title="Minero Pro | Estadísticas", favicon="assets/minero-pro.svg", dark=True)
def estadisticas_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')

    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Estadísticas!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('Escenario 1', on_click=lambda: show_scenario_statistics('Scenario00.txt')).classes(button_class)
            ui.button('Escenario 2', on_click=lambda: show_scenario_statistics('Scenario01.txt')).classes(button_class)
            ui.button('Escenario 3', on_click=lambda: show_scenario_statistics('Scenario02.txt')).classes(button_class)
            ui.button('Escenario 4', on_click=lambda: show_scenario_statistics('Scenario03.txt')).classes(button_class)
            ui.button('Escenario 5', on_click=lambda: show_scenario_statistics('Scenario04.txt')).classes(button_class)
            ui.button('Escenario 6', on_click=lambda: show_scenario_statistics('Scenario05.txt')).classes(button_class)
            ui.button('Escenario 7', on_click=lambda: show_scenario_statistics('Scenario06.txt')).classes(button_class)
            ui.button('Escenario 8', on_click=lambda: show_scenario_statistics('Scenario07.txt')).classes(button_class)
            ui.button('Escenario 9', on_click=lambda: show_scenario_statistics('Scenario08.txt')).classes(button_class)
            ui.button('Escenario 10', on_click=lambda: show_scenario_statistics('Scenario09.txt')).classes(button_class)

    get_footer()
