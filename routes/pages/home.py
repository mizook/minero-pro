from nicegui import ui

from routes.footer import get_footer

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page('/', title="Minero Pro | Inicio", favicon="assets/minero-pro.svg", dark=True)
def home_page():
    with ui.element('div').classes('grid place-items-center w-full h-[700px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Bienvenido a Minero Pro!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('Yacimiento Minero', on_click=lambda: ui.navigate.to('/yacimiento-minero')).classes(button_class)
            ui.button('Plan Minero', on_click=lambda: ui.navigate.to('/plan-minero')).classes(button_class)
            ui.button('Estadísticas', on_click=lambda: ui.navigate.to('/estadisticas')).classes(button_class)
            ui.button('Cálculos', on_click=lambda: ui.navigate.to('/calculos')).classes(button_class)

    get_footer()
