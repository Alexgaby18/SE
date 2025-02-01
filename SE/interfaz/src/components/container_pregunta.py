import flet as ft 

class container_pregunta(ft.Container):
    def __init__(self,pregunta):
        self.pregunt = ft.Text(pregunta,
                    style=ft.TextStyle(
                        color=ft.colors.BLUE_GREY_900,
                        font_family="Roboto Condensed",
                        weight=ft.TextThemeStyle.TITLE_MEDIUM,
                        size=28),
                        text_align = ft.TextAlign.CENTER
                        )
        super().__init__()
        self.content = ft.Column([self.pregunt
        ],
        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER)
        self.alignment = ft.alignment.center
        self.margin= 10
        self.padding= 10
        self.bgcolor= ft.Colors.WHITE10
        self.width= 800
        self.height= 250
        self.border_radius= 25
        self.border = ft.border.all(2,ft.Colors.TEAL_900)