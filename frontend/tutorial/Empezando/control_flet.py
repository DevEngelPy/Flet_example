import flet as ft
import time
def hola_mundo(page:ft.Page):
    texto = ft.Text('hello word')
    page.controls.append(texto)
    page.update()
    
def control_row(page:ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text('A'),
            ft.Text('B'),
            ft.Text('C'),
        ])
    )
    
def contador(page:ft.Page):
    #se agrega el texto a la app
    texto = ft.Text()
    page.add(texto)
    #modificacion del conteo
    for i in range(2):
        texto.value = f'tiempo {i}'
        #actualizacion del recorrido
        page.update()
        #tiempo de recorrido de 1 seg
        time.sleep(1)
    
def control_row_dos(page:ft.Page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label='tu nombre: '),
            ft.ElevatedButton(text='mi nombre')
        ])
    )

def ejem_page_update(page:ft.Page):
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
    page.update()
    time.sleep(0.3)
    
def columnas_tru_disabled(page:ft.Page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)
    
def boton_eventos(page:ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
def pedir_nombre(page:ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

def pendiente(page:ft.Page):
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

def menu_desplegable(page:ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)