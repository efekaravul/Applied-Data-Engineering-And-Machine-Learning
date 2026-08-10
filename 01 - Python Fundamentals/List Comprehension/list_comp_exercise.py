#1
sayilar = [sayi for sayi in range(1,101) if sayi % 12 == 0]
print(sayilar)

#2
text = "Hello 12345 World"
rakamlar = [rakam for rakam in text if rakam.isdigit()]
print(rakamlar)

#3
sicakliklar = [10,20,0,-5,-2]
buzlanma_tehlikesi = ["Buzlanma Tehlikesi" if sicaklik <= 0 else sicaklik for sicaklik in sicakliklar]
print(buzlanma_tehlikesi)

#4
ogrenciler = ["ali", "ayşe", "canan"]
notlar = [50,30,60]

liste = [(ogrenciler[i], notlar[i]) for i in range(len(ogrenciler))]
liste_dict = { key:value for (key,value) in liste if value >= 50}
print(liste)
print(liste_dict)

#5
sonuc = [(x, y) for x in range(3) for y in range(3)]
print(sonuc)