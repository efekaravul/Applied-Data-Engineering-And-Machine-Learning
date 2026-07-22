sayilar = [1,3,5,4,32,56]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 15) # Sayılar listesinde ki değerlerin toplamı ve 15 değerini toplar

products = [
    {"title":"iphone 15", "price": 60000},
    {"title":"iphone 16", "price": 70000},
    {"title":"iphone 17", "price": 80000},
    {"title":"iphone 17", "price": 0},
]

toplamFiyat = sum([urun["price"] for urun in products]) # Ürünlerin toplam fiyatını bulur
urunAdeti = [urun for urun in products if urun["price"] > 0]
sonuc = toplamFiyat / len(products)

print(sonuc)