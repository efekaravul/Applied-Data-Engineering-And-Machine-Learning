import pandas as pd
import numpy as np

array = np.random.randn(4,3)
new_df = pd.DataFrame(array, index=["Efe","Cengiz","Buse","Ali"], columns=["Salary", "Age", "Seniority"])
new_df["Extra"] = 10 # Extra isimli bir column ekler ve tüm indexlere 10 değerini atar.
new_df.drop("Extra", axis=1, inplace=True) # inplace = True yapmamızın sebebi varolan df i değiştirmesi için
                                                 # eğer inplace = True yapmazsak sanki yeni bir df oluşturuyormuş gibi
                                                 # yeni bir değişkene df ataması yapar.
new_df.drop("Ali") # Eğer axis belirtmezsek axisin default değeri 0 dır yani Ali isimli satırı siler.
print(new_df.loc["Efe","Salary"]) # Efenin salary columunu getirir.
new_df.loc["Efe","Salary"] = 100 # Efenin Salary değerini 100 yapar.
print(new_df[new_df > 0]) # Dataframedeki 0 dan büyük olan değerleri çıktı olarak döndürür.



