import flet as ft 

class container_ctenoforos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/ctenoforos.jpg',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Un ctenóforo, a veces llamado "falsa medusa", es un animal marino gelatinoso y transparente, conocido por su belleza iridiscente. A diferencia de las medusas, los ctenóforos no poseen células urticantes (no pican). En cambio, tienen unas células especiales llamadas coloblastos que les permiten capturar a sus presas. Su característica más distintiva son las hileras de "peines" que recorren su cuerpo, compuestos por miles de cilios que se mueven coordinadamente, creando un efecto luminoso que les ha valido el apodo de "criaturas de cristal". ',
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