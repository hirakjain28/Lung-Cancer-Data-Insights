import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_treatment_duration_by_stage(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df,
        x='cancer_stage',
        y='treatment_duration_days',
        estimator=np.mean,
        ci=None,
        palette='viridis'
    )
    plt.title('Average Treatment Duration by Cancer Stage')
    plt.xlabel('Cancer Stage')
    plt.ylabel('Average Treatment Duration (days)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
