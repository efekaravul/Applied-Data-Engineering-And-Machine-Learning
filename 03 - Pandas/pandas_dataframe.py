import pandas
import pandas as pd
import numpy as np

array = np.random.randn(4,3)

df = pd.DataFrame(array) # 4x3 matrixi excel dosyası gibi çıktıya çevirir.

print(df)

data_frame = pd.DataFrame(array, index=["Efe","Cengiz","Ali","Buse"], columns=["Maaş","Yaş","Mail"]) #Satırlara indexler yazılır.
print(data_frame)                                                                                    #Sütunlara columnslar yazılır.
print(data_frame["Maaş"]) # Sadece maaş sütununu çıktı olarak döndürür.
print(data_frame[["Maaş", "Yaş"]]) # Eğer birden fazla sütun getirmek istiyorsak liste içine liste yazarak sütun adlarını yazıyoruz.
print(data_frame.loc["Efe"]) # İstediğimiz satırı görüntelemek için .loc() methodunu kullanıyoruz.
print(data_frame.iloc[0]) # Index numarası 0 olan satırın column bilgilerini getirir.
print(data_frame.iloc[:,1]) # Tüm satırların index numarası 1 olan columnunu çıktı olarak getirir.
