import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


""" Características de Entrada (features)
Podríamos considerar las siguientes características para cada organismo:

Multicelular (0: No, 1: Sí)

Con tejidos verdaderos (0: No, 1: Sí)

Simetría (0: Asimétrica, 1: Radial, 2: Bilateral)

Tipo de cavidad corporal (0: Ninguno, 1: Pseudocelomada, 2: Celomada)

Con esqueleto (0: No, 1: Exoesqueleto, 2: Endoesqueleto)

Complejidad de sistemas digestivos (0: Incompleto, 1: Completo)

Ambiente (0: Acuático, 1: Terrestre) """

# Características de entrada mejoradas
features = [
    (0, 0, 0, 0, 0, 0, 0),  # Protozoarios
    (1, 0, 1, 0, 0, 0, 0),  # Poríferos
    (1, 1, 1, 0, 0, 0, 0),  # Cnidarios
    (1, 1, 1, 0, 0, 1, 0),  # Ctenóforos
    (1, 1, 2, 0, 0, 0, 0),  # Platelmintos
    (1, 1, 2, 2, 1, 1, 1),  # Anélidos
    (1, 1, 2, 2, 1, 1, 0),  # Moluscos
    (1, 1, 2, 2, 2, 1, 1),  # Artrópodos
    (1, 1, 2, 2, 2, 1, 0),   # Cordados
    (1, 1, 0, 0, 0, 0, 0),   # Equinodermos
    (1, 1, 2, 0, 0, 1, 0),   # Nemertinos
    (1, 1, 2, 1, 0, 1, 0),   # Acantocefalo
    (1, 1, 2, 1, 0, 0, 0)   # asquelmitos
]


targets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12] 

# Convertir listas a arrays de NumPy
features = np.array(features)
targets = np.array(targets)

# modelo con más capas y neuronas
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=13, input_shape=[7], activation='sigmoid'),  # Primera capa oculta con 16 neuronas
])

# Compilar el modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print('Inicio de entrenamiento...')
historial = modelo.fit(features, targets, epochs=50, verbose=True)
print('Modelo entrenado!')



modelo.save('phylum_model_mejorado.h5')
