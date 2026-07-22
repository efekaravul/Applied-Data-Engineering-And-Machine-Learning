urunler = [
    {"ad": "Laptop", "fiyat": 25000, "stok": 15},
    {"ad": "Klavye", "fiyat": 800, "stok": 0},
    {"ad": "Mouse", "fiyat": 450, "stok": 50},
    {"ad": "Monitör", "fiyat": 5500, "stok": 8},
    {"ad": "Kulaklık", "fiyat": 1200, "stok": 0}
]

stoktaki_urunler = list(filter(lambda u: u["stok"] > 0, urunler))
isimler = list(map(lambda u: u["ad"].upper(), urunler))
sirali_urunler = sorted(stoktaki_urunler, key=lambda u: u["fiyat"])

print(sirali_urunler)
print(isimler)

araclar = [
    {"marka": "Ford", "fiyat": 450000.55, "hasar_kaydi": True},
    {"marka": "Renault", "fiyat": 320500.25, "hasar_kaydi": False},
    {"marka": "Toyota", "fiyat": 610000.89, "hasar_kaydi": False},
    {"marka": "Fiat", "fiyat": 280000.00, "hasar_kaydi": True},
    {"marka": "Honda", "fiyat": 550000.45, "hasar_kaydi": False}
]

en_pahali = max(araclar, key=lambda u: u["fiyat"])
en_ucuz = min(araclar, key=lambda u: u["fiyat"])
print(en_pahali)
print(en_ucuz)

toplam = sum(arac["fiyat"] for arac in araclar)
ort = toplam / len(araclar)
print(ort)

hasar_kaydi_var_mi = any(arac for arac in araclar if arac["hasar_kaydi"])
print(hasar_kaydi_var_mi)

ikiyuz_ustu_mu = all(bool(arac["fiyat"] > 200000) for arac in araclar)
print(ikiyuz_ustu_mu)