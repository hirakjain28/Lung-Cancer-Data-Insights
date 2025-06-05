import pandas as pd

# -------------------------------
# Load and Preprocess Dataset
# -------------------------------
from preprocessing.feature_engineering import add_treatment_duration

# Load dataset
df = pd.read_csv('dataset_med.csv')  # Make sure dataset is under 'data/' folder
df = add_treatment_duration(df)           # Add treatment_duration_days

# -------------------------------
# Import Feature Modules
# -------------------------------
from features.age_feature import process_age_feature
from features.bmi_feature import process_bmi_feature
from features.cholesterol_feature import process_cholesterol_feature
from features.clustering_feature import process_clustering_feature

# -------------------------------
# Import Visualization Modules
# -------------------------------
from visualizations.treatment_duration_plot import plot_treatment_duration_by_stage

# -------------------------------
# Feature Analysis Menu
# -------------------------------
def main_menu():
    global df
    while True:
        print("\n📊 Feature Analysis Menu")
        print("1. Analyze Age Feature")
        print("2. Analyze BMI Feature")
        print("3. Analyze Cholesterol Feature")
        print("4. Analyze Clustering Feature")
        print("5. Visualize Treatment Duration by Cancer Stage")
        print("6. Save Processed Dataset")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            df = process_age_feature(df)
        elif choice == '2':
            df = process_bmi_feature(df)
        elif choice == '3':
            df = process_cholesterol_feature(df)
        elif choice == '4':
            df = process_clustering_feature(df)
        elif choice == '5':
            plot_treatment_duration_by_stage(df)
        elif choice == '6':
            df.to_csv('data/dataset_med_processed.csv', index=False)
            print("✅ Dataset saved as 'data/dataset_med_processed.csv'")
        elif choice == '7':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    main_menu()
