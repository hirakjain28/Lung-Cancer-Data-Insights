# features/age_feature.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_age_feature(df):
    # Create Age Group
    df['AgeGroup'] = pd.cut(df['age'],
                            bins=[0, 40, 60, 80, 100],
                            labels=['<40', '40-60', '60-80', '80+'])

    # Plot Age distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Plot Age group counts
    plt.figure(figsize=(8, 5))
    sns.countplot(x='AgeGroup', data=df, palette='Set2')
    plt.title('Count of Patients by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    return df
