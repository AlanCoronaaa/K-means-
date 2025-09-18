import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Cargar datos
df = pd.read_csv('Facebook_Live_Sellers.csv')

# Eliminar variables que no sirven
df = df.drop(['status_id', 'status_published'], axis=1)

# Escalar variables
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Determinar valor de k
silhouette_scores = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k)
    cluster_labels = kmeans.fit_predict(df_scaled)
    silhouette_avg = silhouette_score(df_scaled, cluster_labels)
    silhouette_scores.append(silhouette_avg)

plt.plot(range(2, 10), silhouette_scores)
plt.xlabel('Valor de k')
plt.ylabel('Puntuación de Silhouette')
plt.show()

# Seleccionar valor de k
k = 5

# Calcular centros del algoritmo k-means
kmeans = KMeans(n_clusters=k)
kmeans.fit(df_scaled)
centros = kmeans.cluster_centers_

print("Centros:")
print(centros)