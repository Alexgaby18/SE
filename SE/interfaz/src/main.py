import flet as ft
from flet import Page, Text, ElevatedButton, Column, Row, Image, Container, border_radius, padding, margin
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
from components.boton_atras import boton_atras
import tensorflow as tf
import numpy as np

modelo = tf.keras.models.load_model("../../phylum_model_mejorado.h5")

etiquetas_phylum = [
    "Protozoarios", 
    "Poríferos", 
    "Cnidarios", 
    "Ctenóforos", 
    "Platelmintos", 
    "Anélidos", 
    "Moluscos", 
    "Artrópodos", 
    "Cordados",
    "Equinodermos", 
    "Nemertinos", 
    "Acantocefalo", 
    "Asquelmitos"
]

def predecir_phylum(caracteristicas):
    caracteristicas = np.array(caracteristicas).reshape(1, -1)
    # Realizar la predicción 
    prediccion_numerica = modelo.predict(caracteristicas)
    # Obtener el índice de la clase con la mayor probabilidad
    phylum_indice = np.argmax(prediccion_numerica)

    # Mapear el índice de vuelta a la etiqueta del phylum
    phylum_predicho = etiquetas_phylum[phylum_indice]
    # Obtener el porcentaje de certeza
    certeza = np.max(prediccion_numerica) * 100
    return {"phylum_predicho": phylum_predicho, "prediccion_numerica": prediccion_numerica, "certeza": certeza}


# Página de inicio
def pagina_inicio(page: ft.Page):
    page.title = "Sistema de Identificación de Phylum"
    page.theme_mode = 'light' #Modo de la pagina

    # Crear los componentes de la interfaz
    titulo = Text("Sistema de Identificación de Phylum", size=75, weight="bold", font_family="Roboto Condensed",color=ft.colors.BLUE_GREY_900)
    boton_iniciar = ElevatedButton("Iniciar", color=ft.colors.WHITE, on_click=lambda e: mostrar_pagina_identificacion(page), width=200, height=50, bgcolor=ft.colors.BLUE_900)

    # Configurar la imagen de fondo con bordes redondeados
    fondo = Image(src="../assets/phylum.jpg", fit="cover", height=600, width=500, border_radius=20)
    imagen_contenedor = Container(
        content=fondo,
        border_radius=border_radius.all(20),
        padding=padding.all(10),
        margin=margin.all(20)
    )

    # Crear el diseño de la interfaz
    columna_izquierda = Column(
        [titulo, Container(boton_iniciar, alignment=ft.alignment.center)],
        alignment="center",
        spacing=40,
        expand=True
    )

    fila_principal = Row(
        [Container(columna_izquierda, padding=padding.all(40), expand=True), imagen_contenedor],
        alignment="spaceBetween",
        vertical_alignment="center",
        expand=True
    )

    # Agregar margen general a la página
    page.add(Container(fila_principal, padding=padding.all(20)))


def pagina_identificacion(page: ft.Page):

    page.bgcolor = ft.colors.WHITE #Color de fondo de la ventana
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    caracteristicas = [0, 0, 0, 0, 0, 0, 0]  # Características del organismo
 
 #FUNCIONES CAPTURADORAS DE EVENTOS DE LOS BOTONES RESPUESTA
    def Unicelular(e):
        caracteristicas[0] = 0
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_Unicelular)
        page.controls.remove(BotonRespuesta_Multicelular)
        pagina_resultado(page,container_protozoario(), resultado["phylum_predicho"], resultado["certeza"])
        return
    
    def Multicelular(e):
        caracteristicas[0] = 1
        # Pregunta.pregunt.value = "Tu organismo posee tejidos verdaderos?"
        Pregunta.actualizar_pregunta(
            "Tu organismo posee tejidos verdadederos?",
            nuevos_enlaces={"tejidos": "https://academia-lab.com/enciclopedia/tejido-biologia/"}
        )
        page.controls.remove(BotonRespuesta_Unicelular)
        page.controls.remove(BotonRespuesta_Multicelular)
        page.add(BotonRespuesta_No,
                 BotonRespuesta_Si)
        page.update()
        return
    
    def No(e):
        caracteristicas[1] = 0
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_No)
        page.controls.remove(BotonRespuesta_Si)
        pagina_resultado(page,container_poriferos(), resultado["phylum_predicho"], resultado["certeza"])
        return
    
    def Si(e):
        caracteristicas[1] = 1
        # Pregunta.pregunt.value = "Que tipo de simetria tiene tu organismo?"
        Pregunta.actualizar_pregunta(
            "Que tipo de simetria tiene tu organismo?",
            nuevos_enlaces={"simetria": "https://animalesbiologia.com/zoologia/simetria-en-los-animales-tipos-partes"}
        )
        page.controls.remove(BotonRespuesta_No)
        page.controls.remove(BotonRespuesta_Si)
        page.add(BotonRespuesta_RadialSecundario,
                 BotonRespuesta_Radial,
                 BotonRespuesta_Bilateral)
        page.update()
        return
    
    def RadialSecundario(e):
        caracteristicas[2] = 0
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        pagina_resultado(page,container_equinodermos(), resultado["phylum_predicho"], resultado["certeza"])

        return
    
    def Radial(e):
        caracteristicas[2] = 1
        # Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        Pregunta.actualizar_pregunta(
            "Tiene sistema digestivo completo o incompleto?",
            nuevos_enlaces={"digestivo": "https://estudyando.com/sistemas-digestivos-completos-vs-incompletos/"}
        )
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        page.add(BotonRespuesta_RadialCompleto,
                 BotonRespuesta_RadialIncompleto)
        page.update()
        return
    
    def Bilateral(e):
        caracteristicas[2] = 2
        # Pregunta.pregunt.value = "Que tipo de revestimiento tiene?"
        Pregunta.actualizar_pregunta(
            "Que tipo de revestimiento tiene: acelomado, pseudocelomado o celomado?",
            nuevos_enlaces={"acelomado": "https://www.lifeder.com/acelomados/",
            "pseudocelomado": "https://www.lifeder.com/pseudocelomados/",
            "celomado": "https://www.lifeder.com/celoma/"}
        )
        page.controls.remove(BotonRespuesta_RadialSecundario)
        page.controls.remove(BotonRespuesta_Radial)
        page.controls.remove(BotonRespuesta_Bilateral)
        page.add(BotonRespuesta_Acelomados,
                 BotonRespuesta_Pseudocelomados,
                 BotonRespuesta_Celomados)

        page.update()
        return
    
    def RadialCompleto(e):
        caracteristicas[5] = 1 # Sistema digestivo completo
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialCompleto)
        page.controls.remove(BotonRespuesta_RadialIncompleto)
        pagina_resultado(page,container_ctenoforos(), resultado["phylum_predicho"], resultado["certeza"])

        return
    
    def RadialIncompleto(e):
        caracteristicas[5] = 0 # Sistema digestivo incompleto
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_RadialCompleto)
        page.controls.remove(BotonRespuesta_RadialIncompleto)
        pagina_resultado(page,container_cnidarios(),resultado["phylum_predicho"], resultado["certeza"])

        return

    def Acelomados(e):
        caracteristicas[3] = 0
        # Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        Pregunta.actualizar_pregunta(
            "Tiene sistema digestivo completo o incompleto?",
            nuevos_enlaces={"digestivo": "https://estudyando.com/sistemas-digestivos-completos-vs-incompletos/"}
        )
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_AcelomadosCompleto,
                 BotonRespuesta_AcelomadosIncompleto)
        page.update()
        return
    
    def Pseudocelomados(e):
        caracteristicas[3] = 1
        # Pregunta.pregunt.value = "Tiene sistema digestivo completo o incompleto?"
        Pregunta.actualizar_pregunta(
            "Tiene sistema digestivo completo o incompleto?",
            nuevos_enlaces={"digestivo": "https://estudyando.com/sistemas-digestivos-completos-vs-incompletos/"}
        )
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_PseudoCelomadosCompleto,
                 BotonRespuesta_PseudocelomadosIncompleto)
        page.update()
        return

    def Celomados(e):
        caracteristicas[3] = 2
        # Pregunta.pregunt.value = "Son esquixocelomados o enterocelomados?"
        Pregunta.actualizar_pregunta(
            "Son esquizocelomados o enterocelomados?",
            nuevos_enlaces={"esquizocelomados": "https://es.wikipedia.org/wiki/Esquizocelomados",
            "enterocelomados": "https://es.wikipedia.org/wiki/Enterocelomados"}
        )
        page.controls.remove(BotonRespuesta_Acelomados)
        page.controls.remove(BotonRespuesta_Pseudocelomados)
        page.controls.remove(BotonRespuesta_Celomados)
        page.add(BotonRespuesta_Enterocelomados,
                 BotonRespuesta_Esquizocelomados)
        page.update()
        return

    def AcelomadosCompleto(e):
        caracteristicas[5] = 1 # Sistema digestivo completo
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_AcelomadosCompleto)
        page.controls.remove(BotonRespuesta_AcelomadosIncompleto)
        pagina_resultado(page,container_nemertinos(), resultado["phylum_predicho"], resultado["certeza"])

        return
    
    def AcelomadosIncompleto(e):
        caracteristicas[5] = 0 # Sistema digestivo incompleto
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_AcelomadosCompleto)
        page.controls.remove(BotonRespuesta_AcelomadosIncompleto)
        pagina_resultado(page,container_platelmintos(), resultado["phylum_predicho"], resultado["certeza"])

        return

    def PseudocelomadosCompleto(e):
        caracteristicas[5] = 1 # Sistema digestivo completo
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_PseudoCelomadosCompleto)
        page.controls.remove(BotonRespuesta_PseudocelomadosIncompleto)
        pagina_resultado(page,container_acantocefalos(), resultado["phylum_predicho"], resultado["certeza"])

        return

    def PseudocelomadosIncompleto(e):
        caracteristicas[5] = 0 # Sistema digestivo incompleto
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_PseudoCelomadosCompleto)
        page.controls.remove(BotonRespuesta_PseudocelomadosIncompleto)
        pagina_resultado(page,container_asquelmintos(), resultado["phylum_predicho"], resultado["certeza"])

        return

    def Enterocelomados(e):
        caracteristicas[3] = 2
        caracteristicas[4] = 2
        caracteristicas[5] = 1
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_Enterocelomados)
        page.controls.remove(BotonRespuesta_Esquizocelomados)
        pagina_resultado(page,container_cordados(), resultado["phylum_predicho"], resultado["certeza"])
        
        return
    
    def Esquizocelomados(e):
        caracteristicas[3] = 2
        # Pregunta.pregunt.value = "Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?"
        Pregunta.actualizar_pregunta(
            "Tiene manto y concha, esqueleto hidrostatico o exoesqueleto?",
            nuevos_enlaces={"manto": "https://leerciencia.net/los-moluscos-caracteristicas-clasificacion-y-estructura-corporal/",
            "hidrostatico": "https://www.lifeder.com/hidroesqueleto/",
            "exoesqueleto": "https://es.wikipedia.org/wiki/Exoesqueleto"}
        )
        page.controls.remove(BotonRespuesta_Enterocelomados)
        page.controls.remove(BotonRespuesta_Esquizocelomados)
        page.add(BotonRespuesta_MantoYconcha,
                 BotonRespuesta_Esqueleto,
                 BotonRespuesta_Exoesqueleto)
        page.update()
        return

    def MantoYconcha(e):
        caracteristicas[4] = 1
        caracteristicas[5] = 1
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        pagina_resultado(page,container_moluscos(), resultado["phylum_predicho"], resultado["certeza"])
        return
    
    def Esqueleto(e):
        caracteristicas[4] = 1
        caracteristicas[5] = 1
        caracteristicas[6] = 1
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        pagina_resultado(page,container_anelidos(), resultado["phylum_predicho"], resultado["certeza"])
        return
    
    def Exoesqueleto(e):
        caracteristicas[4] = 2
        caracteristicas[5] = 1
        caracteristicas[6] = 1
        resultado = predecir_phylum(caracteristicas)
        page.controls.remove(Pregunta)
        page.controls.remove(BotonRespuesta_MantoYconcha)
        page.controls.remove(BotonRespuesta_Esqueleto)
        page.controls.remove(BotonRespuesta_Exoesqueleto)
        pagina_resultado(page,container_artropodos(), resultado["phylum_predicho"], resultado["certeza"])
        return
    
    #INSTANCIA BOTONES DE RESPUESTA A LAS PREGUNTAS
    
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

    Pregunta = container_pregunta(
        pregunta="¿Tu organismo es unicelular o multicelular?",
        palabras_enlaces={
            "unicelular": "https://concepto.de/organismos-unicelulares/",
            "multicelular": "https://knoow.net/es/ciencias-tierra-vida/biologia-es/organismos-multicelulares/"
        }
    )

    # Mostrar la primera pregunta y los botones
    page.add(Pregunta, BotonRespuesta_Unicelular, BotonRespuesta_Multicelular)

def pagina_resultado(page: ft.Page,contenedor_resultado: ft.Container,phylum: str, certeza: float):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    resultados = ft.Text("RESULTADOS", size=50, weight="bold", font_family="Roboto Condensed",color=ft.colors.BLUE_GREY_900)
    resultado = f'El Phylum determinado es: {phylum} (Certeza: {certeza:.2f}%)'
    phylumDeterminado = ft.Text(resultado,
                    style=ft.TextStyle(
                        color=ft.colors.BLUE_GREY_900,
                        font_family="Roboto Condensed",
                        weight="bold",
                        size=28),
                        text_align = ft.TextAlign.JUSTIFY
                        )
    def regresar(e):
        page.controls.clear()  # Limpiar la página actual
        pagina_inicio(page)  # Reiniciar el ciclo
        page.update()

    botonAtras = boton_atras(on_click=regresar)

    page.controls.clear()
    page.add(resultados, phylumDeterminado,contenedor_resultado,botonAtras)
    page.update()


    return
# Función para cambiar a la página de identificación
def mostrar_pagina_identificacion(page: ft.Page):
    page.controls.clear()  # Limpiar la página actual
    pagina_identificacion(page)  # Mostrar la página de identificación
    page.update()

# Ejecutar la aplicación
ft.app(target=pagina_inicio)