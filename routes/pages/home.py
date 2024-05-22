from nicegui import ui

from routes.constants import mining_deposit_path, mining_plan_path, calculations_path, statistics_path, home_path
from routes.footer import get_footer
from utils.utils import Utils as utl

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page(home_path, title="Minero Pro | Inicio", favicon=utl.get_app_favicon(), dark=True)
def home_page():
    with ui.element('div').classes('grid place-items-center w-full h-[550px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Bienvenido a Minero Pro!').classes(title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center w-full h-full'):
            ui.button('Yacimiento Minero', on_click=lambda: ui.navigate.to(mining_deposit_path)).classes(button_class)
            ui.button('Plan Minero', on_click=lambda: ui.navigate.to(mining_plan_path)).classes(button_class)
            ui.button('Estadísticas', on_click=lambda: ui.navigate.to(statistics_path)).classes(button_class)
            ui.button('Cálculos', on_click=lambda: ui.navigate.to(calculations_path)).classes(button_class)

    get_footer()
