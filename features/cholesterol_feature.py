# features/cholesterol_feature.py

import matplotlib.pyplot as plt
import seaborn as sns

def process_cholesterol_feature(df):
    # Create Cholesterol Category
    def cholesterol_category(chol):
        if chol < 200:
            return 'Normal'
        elif 200 <= chol < 240:
            return 'Borderline High'
        else:
            return 'High'
    df['CholesterolCategory'] = df['cholesterol_level'].apply(cholesterol_category)

    # Plot Cholesterol distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['cholesterol_level'], bins=20, kde=True, color='limegreen')
    plt.title('Cholesterol Level Distribution')
    plt.xlabel('Cholesterol Level (mg/dL)')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Plot Cholesterol category counts
    plt.figure(figsize=(8, 5))
    sns.countplot(x='CholesterolCategory', data=df,
                   order=['Normal', 'Borderline High', 'High'],
                   palette='pastel')
    plt.title('Count of Patients by Cholesterol Category')
    plt.xlabel('Cholesterol Category')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    return df
