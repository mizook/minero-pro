from nicegui import ui

from routes.constants import home_path


def get_go_back_button():
    ui.link('<- Volver atrás', home_path).classes('text-yellow-8')
