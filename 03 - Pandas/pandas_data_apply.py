import pandas as pd
import numpy as np
from openpyxl.reader.excel import load_workbook

df = pd.read_csv("../07 - Machine Learning/Data/8-apply_function_data.csv")

def salary_category(salary):
     if salary < 50000:
         return "Low"
     elif 50000 <= salary < 80000:
         return "Medium"
     else:
        return "High"

df["Salary_Category"] = df["Salary"].apply(salary_category) # Salary_Category adında yeni bir column ekler. Columnun
print(df)                                                   # değerleri yukarıda yazılan fonksiyon ile belirlenir.

def calculate_performance(experience):
    if experience > 10:
        return 1
    else:
        return 0

df["Add_Performance"] = df["Experience"].apply(calculate_performance)   # Çalışanların deneyim süresine göre
df["New_Performance"] = df["Add_Performance"] + df["Performance_Score"] # Performance_Scoreuna +1 ekler ve New_Performance
print(df)                                                               # adında yeni bir column oluşturur.