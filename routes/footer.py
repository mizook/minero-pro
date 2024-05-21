from nicegui import ui


def get_footer():
    with ui.footer().classes('flex justify-end items-end text-end text-xs mt-5 bg-transparent text-white font-bold'):
        ui.label('© Minero Pro')
        ui.label('|')
        ui.image('assets/github-icon.svg').classes('w-[16px] h-[16px] hover:opacity-80 cursor-pointer')
        ui.label('|')
        ui.link('David Araya', 'https://github.com/Dizkm8')
        ui.link('Marcelo Céspedes', 'https://github.com/ZenkaiRed')
        ui.link('Carlo Ramírez', 'https://github.com/mizook')
        ui.link('Pablo Robledo', 'https://github.com/Pablo-RoVi')
