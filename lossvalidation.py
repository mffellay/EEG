# Aquí se graficarán las pérdidas de validación y entrenamiento ocurridas durante el proceso de creación o
#ajuste del modelo del Autoencoder. Primero se tiene para 5 épocas. 
plt.plot(history.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 5 épocas', fontsize=12) 
plt.legend() 
# Para 15 épocas. 
plt.figure() 
plt.plot(history2.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history2.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 15 épocas', fontsize=12) 
plt.legend() 
# Para 25 épocas. 
plt.figure() 
plt.plot(history3.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history3.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 25 épocas', fontsize=12) 
plt.legend() 
# Para 50 épocas. 
plt.figure() 
plt.plot(history4.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history4.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 50 épocas', fontsize=12) 
plt.legend() 
# Este segmento de código corresponde al ajuste del modelo entrenado a 50 épocas al ingresar una entrada 
# distinta al canal 1. Se utilizó el canal 2 de la señal EEG para poder visualizar el modelo siendo aplicado. 
plt.figure() 
encoded_data = autoencoder.encoder(atest_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
encoded_data = autoencoder.encoder(atest_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
plt.plot(atest_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input prueba Ch2.", "Reconstrucción"]) 
plt.show() 
