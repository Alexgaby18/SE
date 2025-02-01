import flet as ft

class boton_respuesta(ft.ElevatedButton):
    def __init__(self,textoRespuesta,on_click):
        super().__init__()
        self.text = textoRespuesta
        self.color = ft.colors.WHITE
        self.bgcolor = ft.colors.BLUE_900
        self.width = 400 
        self.height = 30
        self.on_click = on_click