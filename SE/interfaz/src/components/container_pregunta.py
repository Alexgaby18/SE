# components/container_pregunta.py
import flet as ft

class container_pregunta(ft.Container):
    def __init__(self, pregunta: str, palabras_enlaces: dict = None):
        super().__init__()
        self.palabras_enlaces = palabras_enlaces or {}
        self.pregunt = ft.Text(
            spans=self._crear_spans(pregunta),
            style=ft.TextStyle(
                color=ft.colors.BLUE_GREY_900,
                font_family="Roboto Condensed",
                weight=ft.FontWeight.BOLD,
                size=28
            ),
            text_align=ft.TextAlign.CENTER
        )
        
        self.content = ft.Column(
            [self.pregunt],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.alignment = ft.alignment.center
        self.margin = 10
        self.padding = 10
        self.bgcolor = ft.colors.WHITE10
        self.width = 800
        self.height = 250
        self.border_radius = 25
        self.border = ft.border.all(2, ft.colors.TEAL_900)
    
    def _crear_spans(self, pregunta: str) -> list:
        spans = []
        palabras = pregunta.split()
        for palabra in palabras:
            palabra_limpia = palabra.strip(".,¿?¡!")
            if palabra_limpia in self.palabras_enlaces:
                url = self.palabras_enlaces[palabra_limpia]
                spans.append(
                    ft.TextSpan(
                        f"{palabra} ",
                        style=ft.TextStyle(
                            color=ft.Colors.TEAL_ACCENT_700,
                            # decoration=ft.TextDecoration.UNDERLINE
                        ),
                        on_click=lambda e, url=url: e.page.launch_url(url)
                    )
                )
            else:
                spans.append(ft.TextSpan(f"{palabra} "))
        return spans
    
    def actualizar_pregunta(self, nueva_pregunta: str, nuevos_enlaces: dict = None):
        self.palabras_enlaces = nuevos_enlaces or {}
        self.pregunt.spans = self._crear_spans(nueva_pregunta)
        self.pregunt.update()