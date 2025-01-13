import flet as ft 

class container_platelmintos(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column([
            ft.Image(src = '../assets/platelmitos.png',
                     width= 150,
                     height= 150,
                     fit=ft.ImageFit.FILL),
            ft.Text('Un platelminto es un gusano plano, como su nombre indica. Son animales invertebrados que se caracterizan por tener un cuerpo aplanado, como una hoja. No tienen cavidad corporal interna y suelen ser hermafroditas, es decir, cada individuo tiene órganos reproductores masculinos y femeninos. Los platelmintos pueden ser de vida libre, como las planarias que encontramos en aguas dulces, o parásitos, como las tenias que viven en el intestino de otros animales, incluyendo a los humanos. A pesar de su apariencia sencilla, los platelmintos son muy diversos y han desarrollado adaptaciones sorprendentes para sobrevivir en diferentes ambientes.',
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