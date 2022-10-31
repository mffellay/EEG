# Libraries used for K-Means algorithm which are contained in sklearn. 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale 
# Range of samples to utilize for manipulation, in this case the range is [600-850]  
kmeans_datos = filtered[600:850] 
kmeans_promedio=np.average(x) 
kmeans_datos=(kmeans_datos-kmeans_promedio) 
# Range is selected then to be used for the graphics 
kmeans_datos_ax = range(250) 
plt.plot(kmeans_datos_ax, kmeans_datos) 
plt.show()
# Data has to be reshaped into the adequate format for K-Means algorithm 
kmeans_datos=kmeans_datos.reshape(-1,1) 
kmeans_cluster = KMeans(n_clusters = 1).fit(kmeans_datos) 
# Euclidean Distance calculation needs the center of the grouping 
center = kmeans_cluster.cluster_centers_ 
distance= sqrt((kmeans_datos - center)**2) 
order_index = argsort(distance, axis = 0) 
# Sensitivity is selected here, low value = more data to group as anomalies 
indexes = order_index[-20:] 
values = kmeans_datos[indexes] 
# Graph of original signal with the anomalies shown by the K-Means algorithm
plt.plot(kmeans_datos_ax, kmeans_datos) 
plt.scatter(indexes, values, color='r') 
plt.show() 
