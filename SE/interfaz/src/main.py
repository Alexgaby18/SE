import flet as ft
from components.container_protozoario import container_protozoario


def main(page: ft.Page):

    page.bgcolor = ft.colors.WHITE #Color de fondo de la ventana

    page.add(
        container_protozoario()) #Pa que vean alguito en la ventana si corren la interfaz :3...
                                 #aun se estan haciendo los demás componentes, comando: flet run

ft.app(main)
