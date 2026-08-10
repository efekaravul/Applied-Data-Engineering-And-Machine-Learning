sayilar = [3,5,6,7,8,10,11,12,23,25,26]
sonuc2 = []
for i in sayilar:
    if(i % 2 == 0):
        sonuc2.append(i)

sonuc = [i for i in sayilar if i % 2 == 0] #Filtreleme var sadece çift sayılar liste içine alınır
sonuc = [i if i % 2 == 0 else "Tek Sayı" for i in sayilar] #Filtreleme yok tüm liste elemanları yazılır fakat tek sayılar yerine "Tek Sayı" yazılır.

print(sonuc)

fiyatlar = [4000,1000,2000,0,5000]
vergiler = []

for i in fiyatlar:
    if i > 0:
        vergiler.append(i * 1.20)

print(vergiler)

vergiler2 = [i * 1.20 for i in fiyatlar if i > 0]

print(vergiler2)
