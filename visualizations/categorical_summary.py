import seaborn as sns
import matplotlib.pyplot as plt

def plot_categorical_summary(df):
    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        plt.figure(figsize=(6,4))
        sns.countplot(data=df, x=col, palette='pastel')
        plt.title(f"Distribution of {col}")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()
