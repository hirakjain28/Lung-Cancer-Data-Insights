
# 🩺 Lung Cancer Patient Data Analysis & Survival Prediction

This project is a comprehensive data-driven analysis and survival prediction model for lung cancer patients using a real-world medical dataset. It involves data cleaning, feature engineering, visualization, clustering, and predictive modeling — all organized modularly for clarity and scalability.

---

## 📁 Project Structure

```
.
├── dataset_med.csv                # Dataset file
├── main.py                        # Main controller script
├── features/                      # Custom feature engineering modules
│   ├── age_feature.py
│   ├── bmi_feature.py
│   ├── cholesterol_feature.py
│   └── clustering_feature.py
├── models/
│   └── survival_predictor.py      # RandomForest survival predictor
├── preprocessing/
│   └── feature_engineering.py     # Treatment duration feature
└── visualizations/                # All data visualization scripts
    ├── categorical_summary.py
    ├── numeric_summary.py
    └── treatment_duration_plot.py
```

---

## 🚀 Features

- 📦 **Data Preprocessing**: Missing value handling, datetime conversion, treatment duration calculation.
- 🔧 **Feature Engineering**: Custom features like BMI, cholesterol level, treatment duration, etc.
- 📊 **Data Visualization**: Interactive and modular visualizations for numeric, categorical, and temporal variables.
- 📌 **Clustering**: Grouping based on cancer stage, treatment type, and smoking status.
- 🧠 **Survival Prediction**: RandomForestClassifier to predict patient survival with model evaluation and feature importance.
- 🧭 **Menu-Driven Interface**: Analyze data step-by-step via a CLI-based interactive menu.

---

## 📈 Sample Visualizations

- Age distribution and survival heatmaps  
- BMI and cholesterol-level boxplots by cancer stage  
- Treatment duration comparisons  
- Confusion matrix and feature importance for survival prediction

---

## 🛠️ How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/hirakjain28/Lung-Cancer-Data-Insights.git
cd Lung-Cancer-Data-Insights
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Run the Project
```bash
python main.py
```

Follow the on-screen menu to analyze features, visualize data, or run the survival prediction model.

---

## 💡 Future Enhancements

- Add more ML models (XGBoost, Logistic Regression)
- Deploy with Streamlit for interactive web access
- Add dashboard support for real-time filtering

---

## 📚 Dataset Info

The dataset used is a medical record of lung cancer patients containing:
- Age, gender, BMI, cholesterol
- Diagnosis and treatment dates
- Cancer stage, smoking status, treatment type
- Survival outcome (target for prediction)

_Source: (https://www.kaggle.com/datasets/amankumar094/lung-cancer-dataset)

---

## 👨‍💻 Author

**Hirak Jain**  
B.Tech CSE (Data Science), Year 2  
Feel free to connect with me on [LinkedIn](www.linkedin.com/in/hirak-jain-2954a228b)  
⭐ If you found this useful, please consider giving the repo a star!
