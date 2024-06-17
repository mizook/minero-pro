from nicegui import ui
from routes.pages import home, mining_deposit, mining_plan, statistics, calculations
from routes.pages.deposit import deposit_options

pages_to_run = [
    home.home_page,
    mining_deposit.mining_deposit_page,
    mining_plan.mining_plan_page,
    statistics.statistics_page,
    calculations.calculations_page,
    deposit_options.deposit_options_page
]


def run_app():
    for page in pages_to_run:
        page()

    ui.run(title="Minero Pro", window_size=(1080, 720), reload=False, native=True)
