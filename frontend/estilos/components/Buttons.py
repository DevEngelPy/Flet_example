import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor  = ft.colors.DEEP_PURPLE_700
        self.color = ft.colors.WHITE24
        self.text = text
        self.on_click = on_click