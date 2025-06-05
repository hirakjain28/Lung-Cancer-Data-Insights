import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess_for_model(df):
    target = 'survived'
    df = df[df[target].notna()]

    # Drop non-numeric or derived string features
    drop_cols = ['id', 'diagnosis_date', 'end_treatment_date', 'AgeGroup', 'CholesterolCategory']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns])

    # Encode remaining categorical columns
    from sklearn.preprocessing import LabelEncoder
    encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le

    return df, encoders

def run_survival_model(df):
    print("\n🧠 Starting Survival Prediction Model...")

    # Preprocess data
    df, encoders = preprocess_for_model(df)
    target = 'survived'

    # Define features and labels
    X = df.drop(columns=[target])
    y = df[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    print("\n🧾 Classification Report:")
    print(classification_report(y_test, y_pred))

    print("📉 Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix - Survival Prediction')
    plt.tight_layout()
    plt.show()

    # Feature importance
    importances = model.feature_importances_
    feature_names = X.columns
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances, y=feature_names)
    plt.title("Feature Importance for Survival Prediction")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.show()

    print("✅ Survival prediction complete.\n")

