import pandas as pd
import numpy as np

df_1 = pd.read_csv("../07 - Machine Learning/Data/7-merge_data1.csv")
df_2 = pd.read_csv("../07 - Machine Learning/Data/7-merge_data2.csv")

print(df_1)

#df_1 çıktısı

#    Employee_ID    Name Department
# 0            1   Emp_1         IT
# 1            2   Emp_2         HR
# 2            3   Emp_3         IT
# 3            4   Emp_4  Marketing
# 4            5   Emp_5  Marketing
# 5            6   Emp_6         IT
# 6            7   Emp_7         IT
# 7            8   Emp_8         IT
# 8            9   Emp_9  Marketing
# 9           10  Emp_10  Marketing

print(df_2)

#df_2 çıktısı

#    Employee_ID  Salary  Experience
# 0            5   55658           3
# 1            1  114478           5
# 2           12   48431          19
# 3           10   32747           7
# 4            6   89150           9
# 5           13   95725           7
# 6            9   65773           4
# 7           11   86886          18

# Merge Outer Join

df_merge_outer = pd.merge(df_1, df_2, on="Employee_ID", how="outer") # Outer Merge tüm tabloyu birleştirir ve olmayan
                                                                     # değerler yerine NaN (Boş değer) yazılır.

# Merge Left Join

df_merge_left = pd.merge(df_1, df_2, on="Employee_ID", how="left") # Left join df_1 e göre birleştirir. Örneğin df_2 de
                                                                   # bulunan Emp_13, Emp_12 bu framede bulunmaz. Emp_3
                                                                   # ilk framede vardır fakat ikinci framede olmasa bile
                                                                   # birleştirilip Salary ve Experience a NaN değerler
                                                                   # atanır

# Merge Right Join

df_merge_right = pd.merge(df_1, df_2, on="Employee_ID", how="right") # Üstteki açıklamanın aynısını df_2 ye göre yapar
                                                                     # df_2 de bulunmayan hiçbir Emp merge edilmiş
                                                                     # framede bulunmaz.

# Merge Inner Join

df_merged = pd.merge(df_1, df_2, on="Employee_ID", how="inner") # Outer Joinin tam tersi olarak sadece ortak olan Empleri
                                                                # alır. Örneğin Emp_1 ve Emp_5 bu framede bulunur.



