# Model training and validation loss graph for 5, 15, 25 and 50 epochs 
plt.plot(history.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 5 épocas', fontsize=12) 
plt.legend() 
# 15 epochs 
plt.figure() 
plt.plot(history2.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history2.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 15 épocas', fontsize=12) 
plt.legend() 
# 25 epochs 
plt.figure() 
plt.plot(history3.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history3.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 25 épocas', fontsize=12) 
plt.legend() 
# 50 epochs. 
plt.figure() 
plt.plot(history4.history["loss"], label="Pérdida entrenamiento") 
plt.plot(history4.history["val_loss"], label="Pérdida validación") 
plt.title('Pérdidas en 50 épocas', fontsize=12) 
plt.legend() 
# Model fit test after 50 epochs and graph.
# Channel 2 was used for visualization. 
plt.figure() 
encoded_data = autoencoder.encoder(atest_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
encoded_data = autoencoder.encoder(atest_data).numpy() 
decoded_data = autoencoder.decoder(encoded_data).numpy() 
plt.plot(atest_data, 'b') 
plt.plot(decoded_data, 'r') 
plt.legend(labels=["Input prueba Ch2.", "Reconstrucción"]) 
plt.show() 
