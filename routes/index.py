from nicegui import native, ui
from routes.pages import home, yacimiento_minero, plan_minero, statistics, calculos

pages_to_run = [
    home.home_page,
    yacimiento_minero.yacimiento_minero_page,
    plan_minero.plan_minero_page,
    statistics.statistics_page,
    calculos.calculos_page
]


def run_app():
    for page in pages_to_run:
        page()

    ui.run(reload=False, native=True)
