import pandas as pd
import numpy as np

weather_df = pd.read_excel("../Data/6-weather.xlsx")

print(weather_df.head()) # İlk 5 veriyi gösterir
print(weather_df.tail()) # Son 5 veriyi gösterir.
print(weather_df.info()) # Veri seti hakkında bilgi verir.
print(weather_df.describe()) # Veri seti hakkında detaylı (ortalama,standart sapma,çeyreklikler,yüzdelikler,max) bilgi verir.
print(weather_df.count()) # Kaç data olduğunu gösterir.
print(weather_df.isna()) # Boş, missing data var mı onu gösterir.
