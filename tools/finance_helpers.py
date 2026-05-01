import pandas as pd
import numpy as np

def calculate_cagr(start_value, end_value, periods):
    """
    Calculate Compound Annual Growth Rate.
    """
    if start_value <= 0 or periods <= 0:
        return 0
    return (end_value / start_value) ** (1 / periods) - 1

def detect_outliers(df, column):
    """
    Detect outliers in a dataframe column using IQR.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

if __name__ == "__main__":
    print("Finance Tools loaded.")
