filtered = butter_bandpass_filter(outputSignal[1], lowcut=2, highcut=35, fs=250, order=6) 
filtered2=butter_bandpass_filter(outputSignal[2], lowcut=2, highcut=35, fs=250, order=6) 
train_data=filtered[600:900] 
test_data=filtered[100:350] 
atrain_data=filtered2[600:900] 
atest_data=filtered2[100:350] 
min_val = tf.reduce_min(train_data) 
max_val = tf.reduce_max(train_data) 
train_data =(train_data - min_val) / (max_val - min_val) 
test_data = (test_data - min_val) / (max_val - min_val) 
train_data = tf.cast(train_data, tf.float32) 
test_data = tf.cast(test_data, tf.float32) 
atrain_data =(atrain_data - min_val) / (max_val - min_val) 
atest_data = (atest_data - min_val) / (max_val - min_val) 
atrain_data = tf.cast(atrain_data, tf.float32) 
atest_data = tf.cast(atest_data, tf.float32)

#Se realiza el gráfico de las muestras que se utilizarán para entrenar el modelo. 
plt.figure(figsize=(16,10)) 
plt.grid() 
plt.plot(np.arange(300), train_data) 
plt.title("EEG") 
plt.show()

# Se inicializa el Autoencoder bajo un modelo de detección de anomalías. Se utiliza el modelo secuencial de 
# Tensorflow Keras que transforma capas a objetos con características de entrenamiento e inferencia. Las capas 
# a utilizar son del tipo “RElu” o Rectified Linear Unit Activation (Activación de unidad lineal rectificada). El
# resultado corresponde a una codificación y decodificación de datos que corresponderán al modelo entrenado. 
class AnomalyDetector(Model): 
  def __init__(self): 
    super(AnomalyDetector, self).__init__() 
    self.encoder = tf.keras.Sequential([ 
      layers.Dense(32, activation="relu"), 
      layers.Dense(16, activation="relu"), 
      layers.Dense(8, activation="relu")]) 
    self.decoder = tf.keras.Sequential([ 
      layers.Dense(16, activation="relu"), 
      layers.Dense(32, activation="relu"), 
      layers.Dense(140, activation="sigmoid")]) 
  def call(self, x): 
    encoded = self.encoder(x) 
    decoded = self.decoder(encoded) 
    return decoded 
# Aquí se llama entonces a la clase definida anteriormente del Autoencoder, utilizando un optimizador llamado
# “Adam” que corresponde a un método de gradiente descendente estocástico, siendo este un método iterativo 
# para optimizar una función objetiva basada en la suavidad de la señal. La pérdida a calcular se basa en “mae”
# Mean Absolute Error o Error Absoluto Promedio. 
autoencoder = AnomalyDetector() 
autoencoder.compile(optimizer='adam', loss='mae') 
# Aquí se realiza el fit o ajuste del modelo entrenado según el número de épocas. Una época es una iteración por
# todos los datos de 0 a 100%. Se realiza entonces para 5 épocas. 
history = autoencoder.fit(train_data, train_data,
          epochs=5,  
          batch_size=64, 
          validation_data=(test_data, test_data), 
          shuffle=True) 
encoded_data = autoencoder.encoder(test_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
# Se procede a graficar el input correspondiente a los datos de prueba, como también la información
# decodificada, correspondiente al modelo entrenado, llamado “Reconstrucción”. 
plt.title('Entrada y Reconstrucción Autoencoder 5 épocas ', fontsize=12) 
plt.plot(test_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input", "Reconstruccion"]) 
plt.show() 
# Se realiza el ajuste para 15 épocas y se grafica de igual manera a la anterior. 
history2 = autoencoder.fit(train_data, train_data,  
          epochs=15,  
          batch_size=64, 
          validation_data=(test_data, test_data), 
          shuffle=True) 
plt.figure() 
encoded_data = autoencoder.encoder(test_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
plt.title('Entrada y Reconstrucción Autoencoder 15 épocas ', fontsize=12) 
plt.plot(test_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input", "Reconstruccion"]) 
plt.show() 
# Se realiza el ajuste para 25 épocas y se grafica.
history3 = autoencoder.fit(train_data, train_data,  
          epochs=25,  
          batch_size=64, 
          validation_data=(test_data, test_data), 
          shuffle=True) 
plt.figure() 
encoded_data = autoencoder.encoder(test_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
plt.title('Entrada y Reconstrucción Autoencoder 25 épocas ', fontsize=12) 
plt.plot(test_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input", "Reconstruccion"]) 
plt.show() 
# Se realiza el ajuste para 50 épocas y se grafica. 
history4 = autoencoder.fit(train_data, train_data,  
          epochs=50,  
          batch_size=64, 
          validation_data=(test_data, test_data), 
          shuffle=True) 
plt.figure() 
encoded_data = autoencoder.encoder(test_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
plt.title('Entrada y Reconstrucción Autoencoder 50 épocas', fontsize=12) 
plt.plot(test_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input", "Reconstruccion"]) 
plt.show() 
