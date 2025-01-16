import tensorflow as tf
import numpy as np 

# Cargar el modelo
modelo = tf.keras.models.load_model("phylum_model_mejorado.h5")

# Nombres de los grupos
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
    "Equinodermos"  # Agregar Equinodermos
]

# Función para realizar predicciones
def predecir_phylum(caracteristicas):
    caracteristicas = np.array(caracteristicas).reshape(1, -1)
    # Realizar la predicción
    prediccion_numerica = modelo.predict(caracteristicas)
    # Obtener el índice de la clase con la mayor probabilidad
    phylum_indice = np.argmax(prediccion_numerica)

    """""
    if caracteristicas[0, 2] == 1:  # Simetría radial secundaria
        phylum_indice = 9  # Índice de Equinodermos
    elif caracteristicas[0, 2] == 2 and caracteristicas[0, 5] == 1:  # Simetría radial y digestivo completo
        phylum_indice = 3  # Índice de Ctenóforos
    """

    # Mapear el índice de vuelta a la etiqueta del phylum
    phylum_predicho = etiquetas_phylum[phylum_indice]
    # Obtener el porcentaje de certeza
    certeza = np.max(prediccion_numerica) * 100
    return {"phylum_predicho": phylum_predicho, "prediccion_numerica": prediccion_numerica, "certeza": certeza}

# Función para clasificar el phylum basado en reglas
def clasificar_phylum(caracteristicas):
    multicelular, tejidos_verdaderos, simetria, cavidad, esqueleto, digestivo, ambiente = caracteristicas

    if multicelular == 0:
        return 0  # Protozoarios
    elif multicelular == 1 and tejidos_verdaderos == 0:
        return 1  # Poríferos
    elif multicelular == 1 and tejidos_verdaderos == 1:
        if simetria == 1:  # Simetría radial secundaria
            return 9  # Equinodermos
        elif simetria == 2:  # Simetría radial
            if digestivo == 1:  # Sistema digestivo completo
                return 3  # Ctenóforos
            else:
                return 2  # Cnidarios
        elif simetria == 3:  # Simetría bilateral
            # Aquí podrías agregar más lógica si deseas clasificar más phyla
            return 10  # Placeholder para más clasificaciones
    elif multicelular == 1 and tejidos_verdaderos == 1:
        if simetria == 2:
            if cavidad == 1:
                return 5  # Anélidos
            elif cavidad == 0:
                return 4  # Platelmintos
            elif cavidad == 2:
                if esqueleto == 1:
                    return 6  # Moluscos
                elif esqueleto == 2:
                    return 7  # Artrópodos
                # Agregar más condiciones si es necesario
                return 8  # Cordados

    return -1  # Clasificación desconocida

# Preguntas
def preguntar():
    caracteristicas = [0, 0, 0, 0, 0, 0, 0]  # Inicializar características
    
    multicelular = input("¿Tu organismo es multicelular? (sí/no): ").strip().lower()
    if multicelular == "no":
        caracteristicas[0] = 0  # Unicelular
    elif multicelular == "si":
        caracteristicas[0] = 1  # Multicelular
        tejidos_verdaderos = input("¿Tu organismo tiene tejidos verdaderos? (sí/no): ").strip().lower()
        caracteristicas[1] = 1 if tejidos_verdaderos == "si" else 0

        if caracteristicas[1] == 1:  # Si tiene tejidos verdaderos
            simetria = input("¿Qué tipo de simetría tiene tu organismo? (1: radial secundaria, 2: radial, 3: bilateral): ").strip()
            caracteristicas[2] = int(simetria) if simetria in ['1', '2', '3'] else 0
            
            if caracteristicas[2] == 1:  # Radial secundaria
                return caracteristicas  # Ya tenemos la clasificación para equinodermos
            elif caracteristicas[2] == 2:  # Radial
                digestivo = input("¿Tu organismo tiene sistema digestivo completo o incompleto? (completo/incompleto): ").strip().lower()
                caracteristicas[5] = 1 if digestivo == "completo" else 0  # Guardar información del sistema digestivo
                return caracteristicas  # Retornar características para ser clasificadas
            elif caracteristicas[2] == 3:  # Bilateral
                # Aquí puedes agregar más preguntas si lo deseas
                pass

            cavidad = input("¿Tu organismo tiene cavidad? (0: no, 1: sí): ").strip()
            caracteristicas[3] = int(cavidad) if cavidad in ['0', '1'] else 0
            
            esqueleto = input("¿Tu organismo tiene esqueleto? (1: interno, 2: externo): ").strip()
            caracteristicas[4] = int(esqueleto) if esqueleto in ['1', '2'] else 0
    else:
        print("Respuesta no válida. Por favor, responde con 'sí' o 'no'.")
        return preguntar()  # Repetir la pregunta

    return caracteristicas

# Ejecutar preguntas y clasificar
caracteristicas_usuario = preguntar()
phylum_resultado = clasificar_phylum(caracteristicas_usuario)

# Mostrar el resultado de clasificación
if phylum_resultado != -1:
    print(f'El phylum clasificado es: {etiquetas_phylum[phylum_resultado]}')
else:
    print("Clasificación desconocida.")

# Realizar la predicción utilizando el modelo
phylum_prediccion = predecir_phylum(caracteristicas_usuario)

# Mostrar el resultado de la predicción
print(f'El phylum predicho es: {phylum_prediccion["phylum_predicho"]}')
print(f'Predicción numérica: {phylum_prediccion["prediccion_numerica"]}')
print(f'Porcentaje de certeza: {phylum_prediccion["certeza"]:.2f}%')
