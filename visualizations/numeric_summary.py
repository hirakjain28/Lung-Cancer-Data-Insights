import seaborn as sns
import matplotlib.pyplot as plt

def plot_numeric_summary(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True, color='skyblue')
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.show()
