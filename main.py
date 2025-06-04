# main.py

import pandas as pd

# Load dataset
df = pd.read_csv('dataset_med.csv')

# Feature modules
from features.age_feature import process_age_feature
from features.bmi_feature import process_bmi_feature
from features.cholesterol_feature import process_cholesterol_feature
from features.clustering_feature import process_clustering_feature


# Menu loop
def main_menu():
    global df
    while True:
        print("\n📊 Feature Analysis Menu")
        print("1. Analyze Age Feature")
        print("2. Analyze BMI Feature")
        print("3. Analyze Cholesterol Feature")
        print("4. Analyze Clustering Feature")
        print("5. Save Processed Dataset")
        print("6. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            df = process_age_feature(df)
        elif choice == '2':
            df = process_bmi_feature(df)
        elif choice == '3':
            df = process_cholesterol_feature(df)
        elif choice == '4':
            df = process_clustering_feature(df)            
        elif choice == '5':
            df.to_csv('dataset_med.csv', index=False)
            print("✅ Dataset saved as 'dataset_med.csv'")
        elif choice == '6':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
