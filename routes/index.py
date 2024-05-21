from nicegui import native, ui
from routes.pages import home, mining_deposit, mining_plan, statistics, calculations

pages_to_run = [
    home.home_page,
    mining_deposit.mining_deposit_page,
    mining_plan.mining_plan_page,
    statistics.statistics_page,
    calculations.calculations_page
]


def run_app():
    for page in pages_to_run:
        page()

    ui.run(reload=False, native=True)
