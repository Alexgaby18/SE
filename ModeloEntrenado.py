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
    "Equinodermos", 
    "Nemertinos", 
    "Acantocefalo", 
    "Asquelmitos"
]

# Función para realizar predicciones
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

def clasificar_phylum(caracteristicas):
    multicelular, tejidos_verdaderos, simetria, cavidad, esqueleto, digestivo, ambiente = caracteristicas

    if multicelular == 0:
        return 0  # Protozoarios
    elif multicelular == 1 and tejidos_verdaderos == 0:
        return 1  # Poríferos
    elif multicelular == 1 and tejidos_verdaderos == 1:
        if simetria == 0:  # Simetría radial secundaria
            return 9  # Equinodermos
        elif simetria == 1:  # Simetría radial
            if digestivo == 1:  # Sistema digestivo completo
                return 3  # Ctenóforos
            else:
                return 2  # Cnidarios
        elif simetria == 2:  # Simetría bilateral
            if cavidad == 2:  # Celomado
                return 6  # Moluscos
            elif cavidad == 0:  # Acelomado
                if digestivo == 1:  # Completo
                    return 10  # Nemertinos
                else:
                    return 4  # Platelmintos
            elif cavidad == 1:  # Pseudocelomado
                if digestivo == 1:  # Completo
                    return 11  # Acantocefalo
                else:
                    return 12  # Asquelmitos
            elif esqueleto == 1:  # Esqueleto hidrostático
                return 5  # Anélidos

    return -1  # Clasificación desconocida

# Preguntas
def preguntar():
    caracteristicas = [0] * 7  # Inicializar características
    
    multicelular = input("¿Tu organismo es multicelular? (si/no): ").strip().lower()
    
    if multicelular not in ["si", "no"]:
        print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")
        return preguntar()  # Repetir la pregunta
    
    caracteristicas[0] = 1 if multicelular == "si" else 0
    
    if caracteristicas[0] == 1:
        tejidos_verdaderos = input("¿Tu organismo tiene tejidos verdaderos? (si/no): ").strip().lower()
        caracteristicas[1] = 1 if tejidos_verdaderos == "si" else 0
        
        if caracteristicas[1] == 1:
            simetria = input("¿Qué tipo de simetría tiene tu organismo? (0: radial secundaria, 1: radial, 2: bilateral): ").strip()
            if simetria not in ['0', '1', '2']:
                print("Opción no válida. Inténtalo de nuevo.")
                return preguntar()
            caracteristicas[2] = int(simetria)

            if caracteristicas[2] == 0:  # Radial secundaria
                return caracteristicas
            elif caracteristicas[2] == 1:  # Radial
                digestivo = input("¿Tu organismo tiene sistema digestivo completo o incompleto? (completo/incompleto): ").strip().lower()
                caracteristicas[5] = 1 if digestivo == "completo" else 0
                return caracteristicas
            elif caracteristicas[2] == 2:  # Bilateral
                cavidad = input("¿Tu organismo tiene cavidad? (0: acelomado/nulo, 1: pseudocelomado/parcial, 2: celomado/completo): ").strip()
                if cavidad in ['0', '1', '2']:
                    caracteristicas[3] = int(cavidad)

                    if caracteristicas[3] == 0:  # Acelomado
                        digestivo_a = input("¿Tu organismo tiene sistema digestivo completo o incompleto? (completo/incompleto): ").strip().lower()
                        caracteristicas[5] = 1 if digestivo_a == "completo" else 0
                    elif caracteristicas[3] == 2:  # Celomado
                        tipo_celomado = input("¿Son esquizocelomados o enterocelomados? (esquizocelomados/enterocelomados): ").strip().lower()
                        if tipo_celomado == "enterocelomados":
                            caracteristicas[3] = 2  # Establecer cavidad como celomado
                            caracteristicas[4] = 2
                            caracteristicas[5] = 1  # Asumir digestivo completo para cordados
                        elif tipo_celomado == "esquizocelomados":
                            caracteristicas[3] = 1  # Establecer cavidad como esquizocelomado
                            # Preguntar más sobre los esquizocelomados
                            tipo_esquizocelomado = input("¿Tiene manto y concha, esqueleto hidrostático o exoesqueleto? (manto y concha/esqueleto hidrostatico/exoesqueleto): ").strip().lower()
                            if tipo_esquizocelomado == "manto y concha":
                                caracteristicas[1] = 1  # Tejidos verdaderos
                                caracteristicas[2] = 2  # Simetría bilateral
                                caracteristicas[3] = 2  # Cavidad celomada
                                caracteristicas[4] = 1  # Esqueleto (exoesqueleto de la concha)
                                caracteristicas[5] = 1  # Sistema digestivo completo
                                return caracteristicas  # Clasificar como Moluscos
                            elif tipo_esquizocelomado == "esqueleto hidrostatico":
                                caracteristicas[1] = 1  # Tejidos verdaderos
                                caracteristicas[2] = 2  # Simetría bilateral
                                caracteristicas[3] = 2  # Cavidad pseudocelomada
                                caracteristicas[4] = 1  # No tiene exoesqueleto
                                caracteristicas[5] = 1  # Sistema digestivo completo
                                caracteristicas[6] = 1
                                return caracteristicas  # Clasificar como Anélidos
                            elif tipo_esquizocelomado == "exoesqueleto":
                                caracteristicas[3] = 2
                                caracteristicas[4] = 2
                                caracteristicas[5] = 1  # Digestivo completo para Artrópodos
                                caracteristicas[6] = 1
                                return caracteristicas  # Clasificar como Artrópodos (Placeholder)
                    elif caracteristicas[3] == 1:  # Pseudocelomado
                        digestivo_b = input("¿Tu organismo tiene sistema digestivo completo o incompleto? (completo/incompleto): ").strip().lower()
                        caracteristicas[5] = 1 if digestivo_b == "completo" else 0

    return caracteristicas

# Ejecutar preguntas y clasificar
caracteristicas_usuario = preguntar()

# Imprimir características para verificar
print("Características ingresadas para la predicción:", caracteristicas_usuario)

# Clasificación manual
phylum_resultado = clasificar_phylum(caracteristicas_usuario)

# Mostrar el resultado de clasificación
if phylum_resultado != -1:
    print(f'El phylum clasificado es: {etiquetas_phylum[phylum_resultado]}')
else:
    print("Clasificación desconocida.")

# Realizar la predicción utilizando el modelo
phylum_prediccion = predecir_phylum(caracteristicas_usuario)

# Mostrar el resultado de predicción
print(f'El phylum predicho es: {phylum_prediccion["phylum_predicho"]}')
print(f'Porcentaje de certeza: {phylum_prediccion["certeza"]:.2f}%')