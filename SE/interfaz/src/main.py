import flet as ft
from components.container_protozoario import container_protozoario
from components.container_pregunta import container_pregunta
from components.boton_respuesta import boton_respuesta


def main(page: ft.Page):

    page.bgcolor = ft.colors.WHITE #Color de fondo de la ventana
    
    def prueba(e):
        print('lalala')

    #BOTONES DE RESPUESTA A LAS PREGUNTAS
    
    #Tu organismo es unicelular o multicelular?
    BotonRespuesta_Unicelular = boton_respuesta('Unicelular', on_click = prueba)
    BotonRespuesta_Multicelular = boton_respuesta('Multicelular', on_click = prueba)
    #Tu organismo posee tejidos verdaderos?
    BotonRespuesta_No = boton_respuesta('No', on_click = prueba)
    BotonRespuesta_Si = boton_respuesta('Si', on_click = prueba)
    #Que tipo de simetria tiene tu organismo?
    BotonRespuesta_RadialSecundario = boton_respuesta('Radial Secundario', on_click = prueba)
    BotonRespuesta_Radial = boton_respuesta('Radial', on_click = prueba)
    BotonRespuesta_Bilateral = boton_respuesta('Bilateral', on_click = prueba)
    #Tiene sistema digestivo completo o imcompleto? (radial)
    BotonRespuesta_RadialCompleto = boton_respuesta('Completo', on_click = prueba)
    BotonRespuesta_RadialIncompleto = boton_respuesta('Incompleto', on_click = prueba)
    #Que tipo de revestimiento tiene?
    BotonRespuesta_Acelomados = boton_respuesta('Acelomados (nulo)', on_click = prueba)
    BotonRespuesta_Pseudocelomados = boton_respuesta('Pseudocelomados(parcial)', on_click = prueba)
    BotonRespuesta_Celomados = boton_respuesta('Celomados (completo)', on_click = prueba)
    #Tiene sistema digestivo completo o incompleto? (Acelomados)
    BotonRespuesta_AcelomadosCompleto = boton_respuesta('Completo', on_click = prueba)
    BotonRespuesta_AcelomadosIncompleto = boton_respuesta('Incompleto', on_click = prueba)
    #Tiene sistema digestivo completo o incompleto? (Pseudocelomados)
    BotonRespuesta_PseudoCelomadosCompleto = boton_respuesta('Completo', on_click = prueba)
    BotonRespuesta_PseudocelomadosIncompleto = boton_respuesta('Incompleto', on_click = prueba)
    #Son esquixocelomados o enterocelomados?
    BotonRespuesta_Enterocelomados = boton_respuesta('Enterocelomados', on_click = prueba)
    BotonRespuesta_Esquizocelomados = boton_respuesta('Esquizocelomados', on_click = prueba)
    #Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?
    BotonRespuesta_MantoYconcha = boton_respuesta('Manto y Concha', on_click = prueba)
    BotonRespuesta_Esqueleto = boton_respuesta('Esqueleto hidrostatico', on_click = prueba)
    BotonRespuesta_Exoesqueleto = boton_respuesta('Exoesqueleto', on_click = prueba)

    Pregunta = container_pregunta('Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?')

    page.add(
        Pregunta,
        BotonRespuesta_MantoYconcha,
        BotonRespuesta_Esqueleto,
        BotonRespuesta_Exoesqueleto) #Pa que vean alguito en la ventana si corren la interfaz :3...
                                 #aun se estan haciendo los demás componentes, comando: flet run

ft.app(main)
