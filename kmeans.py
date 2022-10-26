# Libraries used for K-Means algorithm which are contained in sklearn. 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale 
# Range of samples to utilize for manipulation, in this case the range is [600-850]  
kdatos = filtered[600:850] 
kprom=np.average(x) 
kdatos=(kdatos-kprom) 
# Range is selected then to be used for the graphics 
kdatos_ax = range(250) 
plt.plot(kdatos_ax, kdatos) 
plt.show()
# Data has to be reshaped into the adequate format for K-Means algorithm 
kdatos=kdatos.reshape(-1,1) 
kmeans = KMeans(n_clusters = 1).fit(kdatos) 
# Euclidean Distance calculation needs the center of the grouping 
cent = kmeans.cluster_centers_ 
dist= sqrt((kdatos - cent)**2) 
order_index = argsort(dist, axis = 0) 
# Sensitivity is selected here, low value = more data to group as anomalies 
indexes = order_index[-20:] 
values = kdatos[indexes] 
# Graph of original signal with the anomalies shown by the K-Means algorithm
plt.plot(kdatos_ax, kdatos) 
plt.scatter(indexes, values, color='r') 
plt.show() 
