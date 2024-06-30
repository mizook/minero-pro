from nicegui import ui

from routes.pages import calculation_options, calculations, home, mining_deposit, mining_plan, statistics
from routes.pages.deposit import deposit_options

# Lista de páginas a ejecutar
pages_to_run = [
    home.home_page,
    mining_deposit.mining_deposit_page,
    mining_plan.mining_plan_page,
    statistics.statistics_page,
    calculations.calculations_page,
    calculation_options.calculation_options_page,
    deposit_options.deposit_options_page,
]


def run_app():
    for page in pages_to_run:
        page()

    ui.run(title="Minero Pro", window_size=(1080, 720), reload=False, native=True)
