import flet as ft

def main(page: ft.Page):
    text_control = ft.Text(value="Texto inicial")
    column = ft.Column([text_control])
    button = ft.ElevatedButton(text="Cambiar texto", on_click=button_click)
    column.controls.append(button)
    page.add(column)

    def button_click(e):
        text_control.value = "Nuevo texto"
        page.update()

    ft.app(target=main)