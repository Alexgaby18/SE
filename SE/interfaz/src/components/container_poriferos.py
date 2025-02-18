import flet as ft 

class container_poriferos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/poriferos.jpg',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Un porífero es un animal acuático que carece de órganos y tejidos, se alimenta filtrando el agua que pasa a través de sus poros. Permanecen fijos a una superficie. Su cuerpo está formado por una gran cantidad de células que trabajan juntas y poseen un esqueleto interno que puede ser de calcio o sílice.',
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