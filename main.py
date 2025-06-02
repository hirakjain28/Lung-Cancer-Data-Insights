import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset (replace 'your_dataset.csv' with the actual file name if needed)
df = pd.read_csv('dataset_med.csv')

# Display basic info
print(df.info())

# Show the first few rows
print(df.head())

missing_values = df.isnull().sum()

#Percentage of missing values (to understand severity)
missing_percentage = (df.isnull().sum() / len(df)) * 100

#Combine the above info into one DataFrame for better readability
missing_data_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage (%)': missing_percentage
})

#Display columns with missing data
print(missing_data_summary[missing_data_summary['Missing Values'] > 0])

# Find categorical columns
categorical_cols = df.select_dtypes(include='object').columns
print("Categorical columns:", categorical_cols)

label_encoder = LabelEncoder()

for col in categorical_cols:
    if df[col].nunique() == 2:
        df[col] = label_encoder.fit_transform(df[col])


# One-hot encode all categorical columns
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Create Age Group
df['AgeGroup'] = pd.cut(df['age'],
                        bins=[0, 40, 60, 80, 100],
                        labels=['<40', '40-60', '60-80', '80+'])

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

# Create Cholesterol Level Category
def cholesterol_category(chol):
    if chol < 200:
        return 'Normal'
    elif 200 <= chol < 240:
        return 'Borderline High'
    else:
        return 'High'

df['CholesterolCategory'] = df['cholesterol_level'].apply(cholesterol_category)

# Show the new features
print(df[['age', 'AgeGroup', 'bmi', 'BMICategory', 'cholesterol_level', 'CholesterolCategory']].head())
