sayilar = [1,4,6,32,23,12]
harfler = ['a','c','v','z']
isimler = ['ahmet','ali','ada','yiğit']

sonuc = min(sayilar) 
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)
sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min([len(isim) for isim in isimler]) # Minimum uzunluğa sahip kelimenin harf sayısını döndürür

print(sonuc)