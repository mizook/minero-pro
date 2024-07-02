from nicegui import ui

from routes.pages.deposit import deposit_options
from routes.pages import home, statistics, upl
from routes.pages.plan import mining_plan, plan_options
from routes.pages.calculation import calculation_options, calculations
from routes.pages.deposit import deposit_options, mining_deposit

# Lista de páginas a ejecutar
pages_to_run = [
    home.home_page,
    mining_deposit.mining_deposit_page,
    mining_plan.mining_plan_page,
    statistics.statistics_page,
    calculations.calculations_page,
    calculation_options.calculation_options_page,
    deposit_options.deposit_options_page,
    upl.upl_page,
    plan_options.plan_options_page,
]


def run_app():
    for page in pages_to_run:
        page()

    ui.run(title="Minero Pro", window_size=(1080, 720), reload=False, native=True)
