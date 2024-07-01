import asyncio
import multiprocessing

from nicegui import ui

from app.modeler import open_2d_scenery, open_3d_filtered_scenery, open_3d_scenery
from routes.constants import deposit_path, mining_deposit_path
from routes.footer import get_footer
from utils.ui_commons import UICommons
from utils.utils import Utils as utl

global_axis_value: str = "X"
global_cord_value = 0  # do not type because sometimes could be a string if users tries to input a string

global_rock_type: str = "A"
global_ore_grade_range: dict = {"min": 20, "max": 80}


async def handle_button_click(button, file_name, title, is_2d):
    try:
        int(global_cord_value)
    except ValueError:
        return
    button.props("loading")

    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target=open_2d_scenery if is_2d else open_3d_scenery,
        args=(file_name, title, global_axis_value, global_cord_value, event)
        if is_2d
        else (file_name, title, event),
    )
    process.start()
    await asyncio.to_thread(event.wait)
    button.props(remove="loading")


def create_button(button_title: str, scenario_num: str, is_2d: bool = True):
    file_name = f"Scenario0{scenario_num}.txt"
    title = f"Escenario {scenario_num}"
    button = ui.button(button_title)
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_button_click(button, file_name, title, is_2d)
        ),
    )
    button.classes(UICommons.visualization_button_class)
    return button


def validate_integer_value(value: str) -> str | None:
    try:
        parsed_value = int(value)
        return validate_integer_range(parsed_value)
    except ValueError:
        return "Debes ingresar un número entero."
    return None


def validate_integer_range(value: int) -> str | None:
    if value < -500 or value > 500:
        return "El valor debe ir de -500 a 500."
    return None


def on_axis_value_change(obj: object):
    global global_axis_value
    global_axis_value = obj.value


def on_input_value_change(obj: object):
    global global_cord_value
    global_cord_value = obj.value


def on_rock_type_change(obj: object):
    global global_rock_type
    global_rock_type = obj.value


def on_ore_grade_range_change(obj: object):
    global global_ore_grade_range
    global_ore_grade_range = obj.value


async def handle_view_filtered_scenary_click(button, file_name, title):
    try:
        int(global_cord_value)
    except ValueError:
        return
    button.props("loading")

    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target=open_3d_filtered_scenery,
        args=(file_name, title, global_ore_grade_range, global_rock_type, event),
    )
    process.start()
    await asyncio.to_thread(event.wait)
    button.props(remove="loading")


def display_view_filtered_scenery(scenario_num: str):
    file_name = f"Scenario0{scenario_num}.txt"
    title = f"Escenario {scenario_num} Filtrado"
    button = ui.button("Visualizar escenario filtrado")
    button.on(
        "click",
        lambda _: asyncio.create_task(
            handle_view_filtered_scenary_click(button, file_name, title)
        ),
    )
    button.classes(UICommons.visualization_button_class)
    return button


@ui.page(
    f"{deposit_path}/{{scenery_index}}",
    title="Minero Pro | Escenario de Depósito",
    favicon=utl.get_app_favicon(),
    dark=True,
)
def deposit_options_page(scenery_index: str = "1"):
    ui.link("<- Volver atrás", mining_deposit_path).classes("text-yellow-8")
    with ui.element("div").classes("grid place-items-center w-full h-[550px]"):
        with ui.element("div").classes("inline-flex"):
            ui.label(f"Scenario {scenery_index}").classes(UICommons.title_class)
            ui.image(utl.get_minero_pro_image()).classes("ml-5 w-[42px] h-[42px]")

        with ui.list().classes("grid place-items-center h-full w-max-md mt-10"):
            ui.label("Visualización 3D").classes("text-2xl")
            create_button("Visualizar", scenery_index, is_2d=False)

            ui.label("Visualización 2D").classes("text-2xl mt-10 mb-3")
            with ui.grid().classes("w-full place-items-start"):
                ui.label("Eje de corte").classes("text-lg text-left")
            ui.select(["X", "Y", "Z"], value=global_axis_value).classes(
                "w-full"
            ).on_value_change(callback=on_axis_value_change)
            ui.input(
                "Coordenada de Corte",
                validation=validate_integer_value,
                value=global_cord_value,
            ).classes("w-full my-5").on_value_change(callback=on_input_value_change)

            create_button(
                "Visualizar",
                scenery_index,
                is_2d=True,
            )

            ui.label("Filtrados").classes("text-2xl mt-10 mb-3")
            with ui.grid().classes("w-full place-items-start"):
                ui.label("Filtrar por tipo de Roca").classes("text-lg text-left")
            ui.select(["A", "B"], value=global_rock_type).classes(
                "w-full"
            ).on_value_change(callback=on_rock_type_change)
            with ui.grid().classes("w-full place-items-start mt-10 mb-5"):
                ui.label("Filtrado por rango de Ley").classes("text-lg text-left")
            min_max_range = ui.range(
                min=0, max=100, value=global_ore_grade_range
            ).on_value_change(callback=on_ore_grade_range_change)
            ui.label().bind_text_from(
                min_max_range,
                "value",
                backward=lambda v: f'min: {v["min"]}, max: {v["max"]}',
            ).classes("mb-5")
            display_view_filtered_scenery(scenery_index)
    get_footer()
