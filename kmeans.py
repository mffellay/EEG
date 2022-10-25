# Se importan las librerías a utilizar específicas para el modelo K-medios contenidos en sklearn 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale 
# Se selecciona el rango a utilizar de la señal, las muestras 600 a 850 y se calcula el promedio de estas para luego 
restar este valor a los datos. 
kdatos = filtered[600:850] 
kprom=np.average(x) 
kdatos=(kdatos-kprom) 
# Se establece el rango de estos datos para poder ser graficada la muestra a utilizar 
kdatos_ax = range(250) 
plt.plot(kdatos_ax, kdatos) 
plt.show()
#Se remodelan los datos al adecuado y se inicializa el algoritmo de K-Medios estableciendo como 1 el número
de agrupaciones, al cual se le ajustan los datos. 
kdatos=kdatos.reshape(-1,1) 
kmeans = KMeans(n_clusters = 1).fit(kdatos) 
# Se obtiene el centro de la agrupación para poder realizar el cálculo de la distancia Euclidiana. 
cent = kmeans.cluster_centers_ 
dist= sqrt((kdatos - cent)**2) 
order_index = argsort(dist, axis = 0) 
# Se selecciona la sensibilidad del sistema, a menor valor, mayor será la cantidad de datos que se tomarán como
anomalías, lo cual se verá en el gráfico a continuación como puntos rojos. 
indexes = order_index[-20:] 
values = kdatos[indexes] 
# Se realiza el gráfico de la señal original con los puntos establecidos como anomalías por el algoritmo K-medios
plt.plot(kdatos_ax, kdatos) 
plt.scatter(indexes, values, color='r') 
plt.show() 
