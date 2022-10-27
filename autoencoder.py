filtered = butter_bandpass_filter(outputSignal[1], lowcut=2, highcut=35, fs=250, order=6) 
filtered2=butter_bandpass_filter(outputSignal[2], lowcut=2, highcut=35, fs=250, order=6) 
train_data=filtered[600:900] 
test_data=filtered[100:350] 
atrain_data=filtered2[600:900] 
atest_data=filtered2[100:350] 

min_val = tf.reduce_min(train_data) 
max_val = tf.reduce_max(train_data) 

train_data =tf.cast((train_data - min_val) / (max_val - min_val), tf.float32) 
test_data = tf.cast((test_data - min_val) / (max_val - min_val), tf.float32) 

atrain_data = tf.cast((atrain_data - min_val) / (max_val - min_val), tf.float32) 
atest_data = tf.cast((atest_data - min_val) / (max_val - min_val), tf.float32)

# Graph of samples to be used for autoencoder model training 
plt.figure(figsize=(16,10)) 
plt.grid() 
plt.plot(np.arange(300), train_data) 
plt.title("EEG") 
plt.show()

# Autoencoder initialization under anomaly detection model. Sequential model of Tensorflow Keras. Layers "relu" used are Rectified Linear Unit Activation layers
# The result will be data coded and decoded that will be the trained model 
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
# Optimizer used is called "Adam" corresponding to a Stochastic Gradient Descent, being this an iterative method of objective function optimization
# Based on signal smoothing. Loss is calculated using the “mae” oe Mean Absolute Error. 
autoencoder = AnomalyDetector() 
autoencoder.compile(optimizer='adam', loss='mae') 
# Trained model fit for the number of epochs will be plotted now
# 1 epoch corresponds to an iteration of data from beginning to end. 5 epoch graph 
history = autoencoder.fit(train_data, train_data,
          epochs=5,  
          batch_size=64, 
          validation_data=(test_data, test_data), 
          shuffle=True) 
encoded_data = autoencoder.encoder(test_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
# Input data corresponds to test data, as well as the decoded information, being the trained model, called “Reconstrucción”. 
plt.title('Entrada y Reconstrucción Autoencoder 5 épocas ', fontsize=12) 
plt.plot(test_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input", "Reconstruccion"]) 
plt.show() 
# 15 epoch adjustment and graph 
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
# 25 epoch adjustment and graph
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
# 50 epoch adjustment and graph 
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
