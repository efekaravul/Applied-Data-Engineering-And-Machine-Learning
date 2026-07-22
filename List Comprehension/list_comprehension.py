sayilar = []

for i in range(5):
    sayilar.append(i * 2)

print(sayilar)

sayilar2 = [i * 2 for i in range(5)]

print(sayilar2)

kurum = "BTK Akademi"

for i in kurum:
    print(i)

sonuc = [i.upper() for i in kurum]

print(sonuc)