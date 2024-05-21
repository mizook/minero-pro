from nicegui import ui

from utils.utils import Utils as utl


def get_footer():
    with ui.footer().classes('flex justify-end items-end text-end text-xs mt-5 bg-transparent text-white font-bold'):
        ui.label('© Minero Pro')
        ui.label('|')
        ui.image(utl.get_github_icon()).classes('w-[16px] h-[16px] hover:opacity-80 cursor-pointer')
        ui.label('|')
        ui.link('David Araya', 'https://github.com/Dizkm8', new_tab=True)
        ui.link('Marcelo Céspedes', 'https://github.com/ZenkaiRed', new_tab=True)
        ui.link('Carlo Ramírez', 'https://github.com/mizook', new_tab=True)
        ui.link('Pablo Robledo', 'https://github.com/Pablo-RoVi', new_tab=True)
