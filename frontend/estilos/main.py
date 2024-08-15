import flet as ft
from components.Buttons import MyButton
from components.Task import Task
from hooks.buttons import event_click
    
def main(page: ft.Page):
    
    page.add(
                Task(text='do laundry'),
                Task(text='cook dinner')
            )


ft.app(target=main)
