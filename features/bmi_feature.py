# features/bmi_feature.py

import matplotlib.pyplot as plt
import seaborn as sns

def process_bmi_feature(df):
    # Create BMI Category
    def bmi_category(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Normal'
        elif 24.9 <= bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obese'
    df['BMICategory'] = df['bmi'].apply(bmi_category)

    # Plot BMI distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['bmi'], bins=20, kde=True, color='salmon')
    plt.title('BMI Distribution')
    plt.xlabel('BMI')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Plot BMI category counts
    plt.figure(figsize=(8, 5))
    sns.countplot(x='BMICategory', data=df,
                   order=['Underweight', 'Normal', 'Overweight', 'Obese'],
                   palette='muted')
    plt.title('Count of Patients by BMI Category')
    plt.xlabel('BMI Category')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    return df
