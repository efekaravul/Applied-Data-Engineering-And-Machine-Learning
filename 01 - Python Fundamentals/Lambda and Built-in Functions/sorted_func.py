from operator import itemgetter

sayilar = [3,54,23,35,12,99,2,43]

sonuc = sorted(sayilar) # Sayılar listesinin sıralanmış halini döndürür
sonuc = sorted(sayilar, reverse=True) # Sayılar listesini büyükten küçüğe sıralar.

users = [
    {"name" : "efekaravul", "posts" : ["post 1"], "email" : "efekaravul@gmail.com"},
    {"name" : "busenurvardar", "posts" : ["post 1", "post 2", "post 3"]},
    {"name" : "cengizhankeskin", "posts" : ["post 1", "post 2"], "email" : "cengizhankeskin26@gmail.com"},
]

sorted_users = sorted(users, key=lambda user: user["name"])
sorted_users = sorted(users, key=lambda user: len(user["posts"])) # Post sayısı en az olan kullanıcıdan en fazlaya sıralar
map_result = list(map(lambda user: user["name"], sorted_users)) # Sıralanan kullanıcıların sadece name bilgilerini yazdırır
print(map_result)
