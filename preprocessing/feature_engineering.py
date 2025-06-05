import pandas as pd

def add_treatment_duration(df):
    """
    Adds a new column 'treatment_duration_days' by calculating the duration between diagnosis and end of treatment.
    """
    df['diagnosis_date'] = pd.to_datetime(df['diagnosis_date'], errors='coerce', dayfirst=True)
    df['end_treatment_date'] = pd.to_datetime(df['end_treatment_date'], errors='coerce', dayfirst=True)
    df['treatment_duration_days'] = (df['end_treatment_date'] - df['diagnosis_date']).dt.days
    return df
