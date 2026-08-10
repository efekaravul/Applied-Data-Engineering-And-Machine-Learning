sayilar = [1,2,3,4,5]
sayilar_str = ["1", "2", "3", "4", "5"]
isimler = ["ali", "ayşe", "burak", "mehmet"]
kullanicilar = [
    {"ad" : "ali", "soyad" : "yılmaz"},
    {"ad" : "efe", "soyad" : "karavul"}
]

sonuc = list(map(lambda sayi: sayi ** 2, sayilar)) # map func sayilar listesi içindeki tüm değerlerin lambda işlemine girmesini sağlar
sonuc = list(map(int, sayilar_str))
sonuc = list(map(str.capitalize, isimler))
sonuc = list(map(lambda kisi: kisi["ad"], kullanicilar))
print(sonuc)