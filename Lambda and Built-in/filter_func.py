sayilar = [1,2,3,-5,-2,-10]

sonuc = list(filter(lambda x: x < 0, sayilar)) #Filter Fonksiyonu listedeki tüm negatif sayıları döndürür.
sonuc2 = list(map(lambda x: x < 0, sayilar))#Map fonksiyonu True False değer döndürür
sonuc = list(filter(lambda x: x % 2 == 0, sayilar))

isimler = ["efe", "buse", "ayşe", "canan", "burak"]
filter_result = list(filter(lambda x: x[0] == "e", isimler)) #Filter ile "e" ile başlayan değerleri döndürürüz.
map_result = list(map(lambda x: x.upper(), filter_result)) #Map ile filter_resultta döndürdüğümüz listi upperlarız.

print(map_result)

user = [
    {"name" : "efekaravul", "posts" : []},
    {"name" : "busenurvardar", "posts" : ["post 1", "post 2"]},
    {"name" : "cengizhankeskin", "posts" : ["post 1", "post 2"]},
]

posts_counter = list(filter(lambda u: len(u["posts"]) > 0, user)) #Filter ile post sayısı 0 dan fazla olanları filtreledik
map_result = list(map(lambda x: x["name"], posts_counter))# Map ile post sayısı 0 dan büyük kullanıcıların name bilgilerini yazdırdık

print(map_result)

sonuc = [u["name"].upper() for u in user if len(u["posts"]) > 0] # yukarıda iki satırda yaptığımız işlemin list-comp ile tek satıra indirgemiş hali
print(sonuc)
