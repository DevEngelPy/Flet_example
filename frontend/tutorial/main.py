import flet as ft
from Empezando.control_flet import *
from Empezando.controles_personalizados import *
import env as VarEnt


def main(page: ft.Page):
    #caracteristicas de la ventana
    page.title = 'tutorial de flet con documentacion oficial!'
    page.window.min_width = VarEnt.MIN_WIDTH_ENV
    page.window.max_width = VarEnt.MAX_WIDTH_ENV
    page.window.min_height = VarEnt.MIN_HEIGTH_ENV
    page.window.max_height = VarEnt.MAX_HEIGTH_ENV

#---------------------
    #control_flet
#---------------------
'''    #funcion 1
    hola_mundo(page)
    #funcion 2
    contador(page)
    #funcion 3
    control_row(page)
    #funcion 4
    control_row_dos(page)
    #funcion 5
    #ejem_page_update(page)
    
    #funcion 6 y 7
    def boton_basico_ejem(e):
        page.add(
            ft.Text('click')
        )
    page.add(ft.ElevatedButton(text="Click me", on_click=boton_basico_ejem))

    def boton_nivel_arriba_ejem(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=boton_nivel_arriba_ejem)]))
    
    #funcion 8
    columnas_tru_disabled(page)
   #funcion 9
    boton_eventos(page)
    #funcion 10
    pedir_nombre(page)
    #funcion 11
    pendiente(page)
    #funcion 12
    menu_desplegable(page)'''

#---------------------
    #control_flet
#---------------------






ft.app(main)
