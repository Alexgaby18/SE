import flet as ft 

class container_equinodermos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/equinodermos.jpg',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Los equinodermos son animales marinos con un aspecto distintivo: su cuerpo suele estar dividido en cinco partes iguales y muchas especies tienen espinas. Carecen de cabeza y tienen un esqueleto interno. Se mueven y respiran gracias a un sistema único de canales llenos de agua.',
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
        self.width= 400
        self.height= 400
        self.border_radius= 10
        self.border = ft.border.all(2,ft.Colors.TEAL_900)