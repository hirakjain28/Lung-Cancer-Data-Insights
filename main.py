# main.py

import pandas as pd

# Load dataset
df = pd.read_csv('dataset_med.csv')

# Import feature modules
from features.age_feature import process_age_feature
from features.bmi_feature import process_bmi_feature
from features.cholesterol_feature import process_cholesterol_feature

# Call feature functions
df = process_age_feature(df)
df = process_bmi_feature(df)
df = process_cholesterol_feature(df)

# Save the updated dataset (optional)
df.to_csv('data/lung_cancer_data_processed.csv', index=False)

print("✅ All feature engineering and visualizations completed!")
