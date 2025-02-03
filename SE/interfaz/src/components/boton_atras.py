import flet as ft 

class boton_atras(ft.ElevatedButton):
    def __init__(self,on_click):
        super().__init__()
        self.text = "Volver al inicio"
        self.color = ft.colors.WHITE
        self.bgcolor = ft.colors.BLUE_900
        self.width = 200 
        self.height = 30
        self.on_click = on_click