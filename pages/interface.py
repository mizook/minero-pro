from nicegui import ui
from PyVistaExample import open_scenary

# Definir estilos para los botones y títulos
button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'

# Crear la interfaz de usuario
@ui.page('/', title="Minero Pro | Inicio", favicon="assets/minero-pro.svg", dark=True)
def index_page():
    with ui.element('div').classes('grid place-items-center w-full h-[720px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Bienvenido a Minero Pro!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('Yacimiento Minero', on_click=lambda: ui.navigate.to('/yacimiento-minero')).classes(button_class)
            ui.button('Plan Minero', on_click=lambda: ui.navigate.to('/plan-minero')).classes(button_class)
            ui.button('Estadísticas', on_click=lambda: ui.navigate.to('/estadisticas')).classes(button_class)
            ui.button('Cálculos', on_click=lambda: ui.navigate.to('/calculos')).classes(button_class)
            
@ui.page('/yacimiento-minero', title="Minero Pro | Yacimiento Minero", favicon="assets/minero-pro.svg", dark=True)
def yacimiento_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')

    
    with ui.element('div').classes('grid place-items-center w-full h-[720px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Yacimiento Minero!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')
        
        with ui.list().classes('grid place-items-center mt-10'):
            ui.button('Visualizar Escenario 1', on_click=lambda: open_scenary('Scenario00.txt')).classes(button_class)
            ui.button('Visualizar Escenario 2', on_click=lambda: open_scenary('Scenario01.txt')).classes(button_class)
            ui.button('Visualizar Escenario 3', on_click=lambda: open_scenary('Scenario02.txt')).classes(button_class)
            ui.button('Visualizar Escenario 4', on_click=lambda: open_scenary('Scenario03.txt')).classes(button_class)
            ui.button('Visualizar Escenario 5', on_click=lambda: open_scenary('Scenario04.txt')).classes(button_class)
            ui.button('Visualizar Escenario 6', on_click=lambda: open_scenary('Scenario05.txt')).classes(button_class)
            ui.button('Visualizar Escenario 7', on_click=lambda: open_scenary('Scenario06.txt')).classes(button_class)
            ui.button('Visualizar Escenario 8', on_click=lambda: open_scenary('Scenario07.txt')).classes(button_class)
            ui.button('Visualizar Escenario 9', on_click=lambda: open_scenary('Scenario08.txt')).classes(button_class)
            ui.button('Visualizar Escenario 10', on_click=lambda: open_scenary('Scenario09.txt')).classes(button_class)
            

@ui.page('/plan-minero', title="Minero Pro | Plan Minero", favicon="assets/minero-pro.svg", dark=True)
def plan_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')
    
    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Plan Minero!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')
        
        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)

@ui.page('/estadisticas', title="Minero Pro | Estadísticas", favicon="assets/minero-pro.svg", dark=True)
def plan_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')
    
    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Estadísticas!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)
            
@ui.page('/calculos', title="Minero Pro | Cálculos", favicon="assets/minero-pro.svg", dark=True)
def plan_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')
    
    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Cálculos!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')
            
        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)


def run_app():
    ui.run()

if __name__ == "__main__":
    run_app()
