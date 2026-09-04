import pandas as pd
import numpy as np

df = pd.read_csv("../07 - Machine Learning/Data/6-employee.csv")
print(df.head())
print(df.describe())
print(df[["Salary","Experience"]].mean()) #Salary ve Experiencesın ortalamasını yazdırır.

df_grouped = df.groupby("Department") # Tüm çalışanları departmanlarına göre gruplar.
print(df_grouped)
print(df_grouped.describe()) # Eğer varsa hesaplanabilen columnları describelar
print(df_grouped["Salary"].mean()) # Departmanlara göre maaşların ortalamasını bulur.

df_grouped_2 = df.groupby("City")
print(df_grouped_2.describe())
print(df_grouped_2["Salary"].mean()) # Şehirlere göre kazanılan maaş ortalamasını hesaplar.

df_new = pd.read_csv("../07 - Machine Learning/Data/6-employee.csv")

print(df_new.head())
print(df_new.describe())