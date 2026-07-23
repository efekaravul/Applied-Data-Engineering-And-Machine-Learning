import pandas as pd
import numpy as np

weather_na_df = pd.read_excel("../Data/6-weatherna.xlsx")


print(weather_na_df.isna()) # Bool tipinde tablo döndürüp NA olan dataları True döndürür.

print(weather_na_df.describe()) # Boş olmayan dataları görmezden gelip diğer datalarla aynı hesaplamaları yapar.

print(weather_na_df["Paris"].count()) # Parisin kaç dataya sahip olduğunu döndürür.

print(weather_na_df.dropna()) # Rowları tarar, eğer rowlarda bir tane bile NA değer varsa rowun tamamını siler.

print(weather_na_df.fillna(weather_na_df.mean())) # Boş olan datalar yerine her ortalama değerlerini atar Örneğin:
                                                  # İstanbulun ortalaması 22 ise İstanbul için 22 Parisin Ortalaması
                                                  # 19 ise Paris için 19 değeri atar.

print(weather_na_df.fillna(weather_na_df["Paris"].median())) # Buradada sadece Parisin boş datalarına Parise ait olan
                                                             # Median değerlerini atar. İstenilen tüm methodlar kullanılabilir
                                                             # max(), min() vb.