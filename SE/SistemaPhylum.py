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
    (1, 1, 1, 0, 0, 0, 1),  # Cnidarios
    (1, 1, 1, 1, 0, 1, 0),  # Ctenóforos
    (1, 1, 2, 0, 1, 0, 1),  # Platelmintos
    (1, 1, 2, 1, 1, 1, 1),  # Anélidos
    (1, 1, 2, 2, 1, 1, 0),  # Moluscos
    (1, 1, 2, 2, 2, 1, 1),  # Artrópodos
    (1, 1, 2, 2, 2, 1, 0),  # Cordados
    (1, 1, 1, 1, 1, 1, 1), # Equinodermosl
]


targets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# Convertir listas a arrays de NumPy
features = np.array(features)
targets = np.array(targets)

# modelo con más capas y neuronas
"""modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=7, input_shape=[7], activation='relu'),  # Primera capa oculta con 16 neuronas
    tf.keras.layers.Dense(units=128, activation='relu'),  # Segunda capa oculta con 32 neuronas
    tf.keras.layers.Dense(units=64, activation='relu'),  # Tercera capa oculta con 16 neuronas
    tf.keras.layers.Dense(units=32, activation='relu'),
    tf.keras.layers.Dense(units=10, activation='softmax')  # Capa de salida con 9 neuronas (una por cada clase)
])"""
input = tf.keras.Input(shape=(7,))
x = tf.keras.layers.Dense(units=128, activation='relu')(input)
x = tf.keras.layers.Dense(units=64, activation='relu')(x)
x = tf.keras.layers.Dense(units=128, activation='relu')(x)
output = tf.keras.layers.Dense(units=10, activation='softmax')(x)

modelo = tf.keras.Model(inputs= input,outputs = output)

# Compilar el modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print('Inicio de entrenamiento...')
historial = modelo.fit(features, targets, epochs=200, batch_size=10, validation_split=0.2, verbose=True)
print('Modelo entrenado!')

# Visualizar la pérdida y la precisión durante el entrenamiento
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.xlabel('#Época')
plt.ylabel('Pérdida')
plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida de validación')
plt.legend()

plt.subplot(1, 2, 2)
plt.xlabel('#Época')
plt.ylabel('Precisión')
plt.plot(historial.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(historial.history['val_accuracy'], label='Precisión de validación')
plt.legend()

plt.show()


modelo.save('phylum_model_mejorado.h5')
