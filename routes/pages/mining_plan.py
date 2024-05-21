from nicegui import ui

from routes.constants import mining_plan_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.utils import Utils as utl

title_class = 'text-4xl font-bold text-center mt-2'
button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black'


@ui.page(mining_plan_path, title="Minero Pro | Plan Minero", favicon=utl.get_app_favicon(), dark=True)
def mining_plan_page():
    get_go_back_button()

    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Plan Minero!').classes(title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)

    get_footer()