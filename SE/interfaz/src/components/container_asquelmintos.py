import flet as ft 

class container_asquelmintos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/asquelmintos.png',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Los asquelmintos son un grupo de gusanos muy diverso que tienen entre sí una característica común y es que todos tienen una sola cavidad en donde están situados los órganos de su cuerpo, sin segmentos ni anillos, aunque algunos exteriormente parecen anillados.',
                    style=ft.TextStyle(
                        color=ft.colors.BLUE_GREY_900,
                        font_family="Roboto Condensed",
                        weight=ft.TextThemeStyle.TITLE_MEDIUM,
                        size=18),
                        text_align = ft.TextAlign.JUSTIFY
                        )
        ],
        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER)
        self.alignment = ft.alignment.center
        self.margin= 10
        self.padding= 10
        self.bgcolor= ft.Colors.WHITE10
        self.width= 300
        self.height= 400
        self.border_radius= 10
        self.border = ft.border.all(2,ft.Colors.TEAL_900)