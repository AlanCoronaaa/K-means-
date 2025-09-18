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
    cluster_labels = kmeans
