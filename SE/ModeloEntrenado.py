import tensorflow as tf
import numpy as np 
modelo = tf.keras.models.load_model("phylum_model_mejorado.h5")

# Función para realizar predicciones
def predecir_phylum(caracteristicas):
    caracteristicas = np.array(caracteristicas).reshape(1, -1)
    # Realizar la predicción
    prediccion_numerica = modelo.predict(caracteristicas)
    # Obtener el índice de la clase con la mayor probabilidad
    phylum_indice = np.argmax(prediccion_numerica)
    # Mapear el índice de vuelta a la etiqueta del phylum
    etiquetas_phylum = ["Protozoarios", "Poriferos", "Cnidarios", "Ctenoforos", "Platelmintos", "Anelidos", "Moluscos", "Artrópodos", "Cordados", "Equinodermos", "Nemertinos", "Acantocefalo", "Asquelmitos"]
    phylum_predicho = etiquetas_phylum[phylum_indice]
    return {"phylum_predicho":phylum_predicho, "prediccion_numerica": prediccion_numerica}

# Probar la función de predicción con un ejemplo
caracteristicas_ejemplo = [1, 1, 2, 1, 0, 0, 0]  # Cambiar según sea necesario
phylum = predecir_phylum(caracteristicas_ejemplo)
print(f'El phylum predicho es: {phylum["phylum_predicho"]}')
print(phylum["prediccion_numerica"])

