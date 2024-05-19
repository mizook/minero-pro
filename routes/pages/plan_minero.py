from nicegui import ui

title_class = 'text-4xl font-bold text-center mt-2'
button_class = 'text-xl font-bold w-[300px] lg:w-[500px] mt-5 bg-yellow-8 text-black' 

@ui.page('/plan-minero', title="Minero Pro | Plan Minero", favicon="assets/minero-pro.svg", dark=True)
def plan_minero_page():
    ui.link('<- Volver atrás', '/').classes('text-yellow-8')
    
    with ui.element('div').classes('grid place-items-center w-full h-[300px]'):
        with ui.element('div').classes('inline-flex'):
            ui.label('¡Plan Minero!').classes(title_class)
            ui.image('assets/minero-pro.svg').classes('ml-5 w-[42px] h-[42px]')
        
        with ui.list().classes('grid place-items-center'):
            ui.button('WORK IN PROGRESS', on_click=lambda: ui.notify('WIP')).classes(button_class)
            
    with ui.footer().classes('flex justify-end items-end text-end text-xs mt-5 bg-transparent text-white font-bold'):
        ui.label('© Minero Pro')
        ui.label('|')
        ui.link('David Araya', 'https://github.com/Dizkm8')
        ui.link('Marcelo Céspedes', 'https://github.com/ZenkaiRed')
        ui.link('Carlo Ramírez', 'https://github.com/mizook')
        ui.link('Pablo Robledo', 'https://github.com/Pablo-RoVi')