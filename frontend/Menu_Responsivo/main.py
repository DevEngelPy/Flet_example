import flet as ft
#tools - herramientas
from flet import (Page, colors)
#modelo
from Trello import TrelloApp

if __name__ == '__main__':
    def main(page: ft.Page):
        #estructura de la ventana
        #titulo
        page.title = 'Trello'
        #espaciado
        page.padding = 0
        #color
        page.bgcolor = colors.BLUE_GREY_200
        #tamaños
        page.window_min_height = 600
        page.window_min_width = 900
        page.window_max_height = 600
        page.window_max_width = 900
        #tema
        page.theme_mode = ft.ThemeMode.DARK
        #clase aplicacion de modelado
        app = TrelloApp(page)
        page.add(app)
        page.update()
   
    

    ft.app(target=main, view=ft.WEB_BROWSER)
