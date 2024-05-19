from nicegui import ui
from routes.pages import home, yacimiento_minero, plan_minero, estadisticas, calculos

pages_to_run = [
    home.home_page,
    yacimiento_minero.yacimiento_minero_page,
    plan_minero.plan_minero_page,
    estadisticas.estadisticas_page,
    calculos.calculos_page
]

def run_app():
    for page in pages_to_run:
        page()
    
    ui.run()
