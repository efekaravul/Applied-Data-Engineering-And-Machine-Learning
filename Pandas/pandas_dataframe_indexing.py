import pandas as pd
import numpy as np

np_array = [[10,20,30],[40,50,60],[70,80,90],[100,110,120]]
df = pd.DataFrame(np_array, index=["Efe","Cengiz","Buse","Ali"], columns=["Salary","Age","Seniority"])

reset_frame = df.reset_index() # Index adında bir column oluşturup bizim index değerlerimizi o columna atar.
                               # Yeni indexler 0 dan row sayısına kadar numaralandırılır

# print(reset_frame.loc["Efe"]) Bu kod artık çalışmaz çünkü python "Efe" diye bir index bulamaz.
print(reset_frame.loc[0]) # İstediğimiz index numarasını yazarak çıktı alabiliriz.

new_indices = ["E", "C", "B", "A"]
df["NewIndex"] = new_indices
print(df)

df.set_index("NewIndex", inplace=True) # Index değerleri Efe,Cengiz,... olmaktan çıkıp E,C,B,A olur. inplace=True
print(df)                                   # yaptığımız içinde asıl DataFrame değişir.

print(df.loc["E"]) # Index değeri E olan columnları getirir.

#Multi Index

first_index = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
inner_index = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]

zipped_index = list(zip(first_index, inner_index))
zipped_index = pd.MultiIndex.from_tuples(zipped_index)

print(zipped_index)

np_array_2 = np.ones(12).reshape(6,2)

big_df = pd.DataFrame(np_array_2, index=zipped_index ,columns=["First", "Second"])
print(big_df)

#                    First  Second       YUKARIDA YAZDIĞIMIZ KODLAR BÖYLE BİR ÇIKTI OLUŞTURUR:
# Simpson    Homer      1.0     1.0      Simpsonlar ve South Park adı altında 2 büyük index
#            Bart       1.0     1.0      ve altlarında Simpson ve South Park index üyeleri bulunur.
#            Marge      1.0     1.0
# South Park Cartman    1.0     1.0
#            Kenny      1.0     1.0
#            Kyle       1.0     1.0

print(big_df.loc["Simpson"]) # Simpsons indexinin altındaki indexleri ve o indexlerin columnlarını getirir.

# print(big_df.loc["Homer"]) Bu kod çalışmaz, "Homer" indexini bu şekilde yazmamız mümkün değil.

print(big_df.loc["Simpson"].loc["Homer"]) # Simpson indexinin altındaki Homer indexinin columnlarını getirir.



