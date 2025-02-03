import flet as ft 

class container_nemertinos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/nemertinos.png',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Un nemertino es un gusano marino alargado y blando, a menudo llamado "gusano cinta". Son animales bastante simples pero fascinantes. Su característica más distintiva es una probóscide retráctil, como una lengua larga y pegajosa, que utilizan para capturar a sus presas.',
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