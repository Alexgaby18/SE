import flet as ft
from components.container_protozoario import container_protozoario
from components.container_poriferos import container_poriferos
from components.container_equinodermos import container_equinodermos
from components.container_ctnoforos import container_ctenoforos
from components.container_cnidarios import container_cnidarios
from components.container_nemertinos import container_nemertinos
from components.container_platelmintos import container_platelmintos
from components.container_acantocefalos import container_acantocefalos
from components.container_asquelmintos import container_asquelmintos
from components.container_cordados import container_cordados
from components.container_moluscos import container_moluscos
from components.container_anelidos import container_anelidos
from components.container_artropodos import container_artropodos
from components.container_pregunta import container_pregunta
from components.boton_respuesta import boton_respuesta


def main(page: ft.Page):

    page.bgcolor = ft.colors.WHITE #Color de fondo de la ventana
 
 #FUNCIONES CAPTURADORAS DE EVENTOS DE LOS BOTONES RESPUESTA
    def Unicelular(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_Unicelular)
        page.controls.remove(BotonRespuesta_Multicelular)
        page.add(container_protozoario())
        page.update()
        return
    
    def Multicelular(e):
        Pregunta.pregunt.value = "Tu organismo posee tejidos verdaderos?"
        page.controls.remove(BotonRespuesta_Unicelular)
        page.controls.remove(BotonRespuesta_Multicelular)
        page.add(BotonRespuesta_No,
                 BotonRespuesta_Si)
        page.update()
        return
    
    def No(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_No)
        page.controls.remove(BotonRespuesta_Si)
        page.add(ft.Column(container_poriferos()))
        return
    
    def Si(e):
        Pregunta.pregunt.value = "Que tipo de simetria tiene tu organismo?"
        page.controls.remove(BotonRespuesta_No)
        page.controls.remove(BotonRespuesta_Si)
        page.add(BotonRespuesta_RadialSecundario,
                 BotonRespuesta_Radial,
                 BotonRespuesta_Bilateral)
        page.update()
        return
    
    def RadialSecundario(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        page.add(container_equinodermos())
        page.update()
        return
    
    def Radial(e):
        Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        page.add(BotonRespuesta_RadialCompleto,
                 BotonRespuesta_RadialIncompleto)
        page.update()
        return
    
    def Bilateral(e):
        Pregunta.pregunt.value = "Que tipo de revestimiento tiene?"
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        page.add(BotonRespuesta_Acelomados,
                 BotonRespuesta_Pseudocelomados,
                 BotonRespuesta_Celomados)

        page.update()
        return
    
    def RadialCompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialCompleto)
        page.controls.remove(BotonRespuesta_RadialIncompleto)
        page.add(container_ctenoforos())
        page.update()
        return
    
    def RadialIncompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialCompleto)
        page.controls.remove(BotonRespuesta_RadialIncompleto)
        page.add(container_cnidarios())
        page.update()
        return

    def Acelomados(e):
        Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_AcelomadosCompleto,
                 BotonRespuesta_AcelomadosIncompleto)
        page.update()
        return
    
    def Pseudocelomados(e):
        Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_PseudoCelomadosCompleto,
                 BotonRespuesta_PseudocelomadosIncompleto)
        page.update()
        return

    def Celomados(e):
        Pregunta.pregunt.value = "Son esquixocelomados o enterocelomados?"
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_Enterocelomados,
                 BotonRespuesta_Esquizocelomados)
        page.update()
        return

    def AcelomadosCompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_AcelomadosCompleto)
        page.controls.remove(BotonRespuesta_AcelomadosIncompleto)
        page.add(container_nemertinos())
        page.update()
        return
    
    def AcelomadosIncompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_AcelomadosCompleto)
        page.controls.remove(BotonRespuesta_AcelomadosIncompleto)
        page.add(container_platelmintos())
        page.update()
        return

    def PseudocelomadosCompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_PseudoCelomadosCompleto)
        page.controls.remove(BotonRespuesta_PseudocelomadosIncompleto)
        page.add(container_acantocefalos())
        page.update()
        return

    def PseudocelomadosIncompleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_PseudoCelomadosCompleto)
        page.controls.remove(BotonRespuesta_PseudocelomadosIncompleto)
        page.add(container_asquelmintos())
        page.update()
        return

    def Enterocelomados(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_Enterocelomados)
        page.controls.remove(BotonRespuesta_Esquizocelomados)
        page.add(container_cordados())
        page.update()
        return
    
    def Esquizocelomados(e):
        Pregunta.pregunt.value = "Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?"
        page.controls.remove(BotonRespuesta_Enterocelomados)
        page.controls.remove(BotonRespuesta_Esquizocelomados)
        page.add(BotonRespuesta_MantoYconcha,
                 BotonRespuesta_Esqueleto,
                 BotonRespuesta_Exoesqueleto)
        page.update()
        return

    def MantoYconcha(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        page.add(container_moluscos())
        page.update()
        return
    
    def Esqueleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        page.add(container_anelidos())
        page.update()
        return
    
    def Exoesqueleto(e):
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        page.add(container_artropodos())
        page.update()
        return
    
    #BOTONES DE RESPUESTA A LAS PREGUNTAS
    
    #Tu organismo es unicelular o multicelular?
    BotonRespuesta_Unicelular = boton_respuesta('Unicelular', on_click = Unicelular)
    BotonRespuesta_Multicelular = boton_respuesta('Multicelular', on_click = Multicelular)
    #Tu organismo posee tejidos verdaderos?
    BotonRespuesta_No = boton_respuesta('No', on_click = No)
    BotonRespuesta_Si = boton_respuesta('Si', on_click = Si)
    #Que tipo de simetria tiene tu organismo?
    BotonRespuesta_RadialSecundario = boton_respuesta('Radial Secundario', on_click = RadialSecundario)
    BotonRespuesta_Radial = boton_respuesta('Radial', on_click = Radial)
    BotonRespuesta_Bilateral = boton_respuesta('Bilateral', on_click = Bilateral)
    #Tiene sistema digestivo completo o imcompleto? (radial)
    BotonRespuesta_RadialCompleto = boton_respuesta('Completo', on_click = RadialCompleto)
    BotonRespuesta_RadialIncompleto = boton_respuesta('Incompleto', on_click = RadialIncompleto)
    #Que tipo de revestimiento tiene?
    BotonRespuesta_Acelomados = boton_respuesta('Acelomados (nulo)', on_click = Acelomados)
    BotonRespuesta_Pseudocelomados = boton_respuesta('Pseudocelomados(parcial)', on_click = Pseudocelomados)
    BotonRespuesta_Celomados = boton_respuesta('Celomados (completo)', on_click = Celomados)
    #Tiene sistema digestivo completo o incompleto? (Acelomados)
    BotonRespuesta_AcelomadosCompleto = boton_respuesta('Completo', on_click = AcelomadosCompleto)
    BotonRespuesta_AcelomadosIncompleto = boton_respuesta('Incompleto', on_click = AcelomadosIncompleto)
    #Tiene sistema digestivo completo o incompleto? (Pseudocelomados)
    BotonRespuesta_PseudoCelomadosCompleto = boton_respuesta('Completo', on_click = PseudocelomadosCompleto)
    BotonRespuesta_PseudocelomadosIncompleto = boton_respuesta('Incompleto', on_click = PseudocelomadosIncompleto)
    #Son esquixocelomados o enterocelomados?
    BotonRespuesta_Enterocelomados = boton_respuesta('Enterocelomados', on_click = Enterocelomados)
    BotonRespuesta_Esquizocelomados = boton_respuesta('Esquizocelomados', on_click = Esquizocelomados)
    #Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?
    BotonRespuesta_MantoYconcha = boton_respuesta('Manto y Concha', on_click = MantoYconcha)
    BotonRespuesta_Esqueleto = boton_respuesta('Esqueleto hidrostatico', on_click = Esqueleto)
    BotonRespuesta_Exoesqueleto = boton_respuesta('Exoesqueleto', on_click = Exoesqueleto)

    Pregunta = container_pregunta('Tu organismo es unicelular o multicelular?')

    page.add(
        Pregunta,
        BotonRespuesta_Unicelular,
        BotonRespuesta_Multicelular) #comando: flet run
ft.app(main)
