from nicegui import ui
from routes.constants import mining_deposit_path
from routes.footer import get_footer
from routes.go_back_button import get_go_back_button
from utils.utils import Utils as utl
from utils.ui_commons import UICommons


def create_button(scenario_num):
    return ui.button(f'Escenario {scenario_num}',
                     on_click=lambda: ui.navigate.to(f"/scenery/{scenario_num}")).classes(
        UICommons.button_class)


@ui.page(mining_deposit_path, title="Minero Pro | Yacimiento Minero", favicon=utl.get_app_favicon(), dark=True)
def mining_deposit_page():
    get_go_back_button()

    with ui.element('div').classes('grid place-items-center w-full h-[500px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Yacimiento Minero!').classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes('ml-5 w-[42px] h-[42px]')

        with ui.list().classes('grid place-items-center grid-cols-2 gap-x-5 mt-10'):
            for index in range(10):
                create_button(index)

    get_footer()
