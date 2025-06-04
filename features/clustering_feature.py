# features/clustering_feature.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def process_clustering_feature(df, n_clusters=3):
    # Step 1: Encode categorical columns
    cols_to_encode = ['cancer_stage', 'smoking_status', 'treatment_type']
    df_encoded = df[cols_to_encode].copy()

    for col in cols_to_encode:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))  # Handle any NaNs

    # Step 2: Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df_encoded)

    # Step 3: Visualize clusters (optional: PCA for better plot)
    sns.pairplot(df_encoded.assign(Cluster=df['Cluster']), hue='Cluster', palette='Set2')
    plt.suptitle("Cluster Visualization Based on Cancer Stage, Smoking Status, and Treatment Type", y=1.02)
    plt.show()

    return df
