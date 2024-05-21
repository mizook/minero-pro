from nicegui import ui

from routes.footer import get_footer
from utils.utils import Utils as utl

button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'
title_class = 'text-4xl font-bold text-center mt-2'


@ui.page('/calculos', title="Minero Pro | Cálculos", favicon=utl.get_app_favicon(), dark=True)
def calculos_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')

    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Cálculos!').classes(title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)

    get_footer()
