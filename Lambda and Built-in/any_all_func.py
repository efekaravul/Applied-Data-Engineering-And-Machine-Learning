sonuc = all([True, True,True])  # AND operatörü gibi çalışma mantığı vardır. True değer döndürür
sonuc = all([False, True,True]) # AND operatörü gibi çalıştığı için bu liste içinde bir false değeri
                                # olması bile döndürülen değerin false olmasını sağlar

sonuc = any([True, True,True])  # OR operatörü gibi çalışma mantığı vardır. True değer döndürür.
sonuc = any([False, True,True]) # OR operatörü gibi çalıştığı için false değer barındırsa bile döndürülen değer
                                # true olur

sayilar = [1,2,3,4,5,6,7,-1]
all_result = all([bool(sayi > 0) for sayi in sayilar]) # Bir tane - değer olduğu için False döndürür
any_result = any([bool(sayi > 0) for sayi in sayilar]) # - değer olsa bile döndürülen değer true olur
print(all_result)
print(any_result)

users = ["ali", "efe", "cengiz"]
all_result_2 = all([bool(user[0] == "e") for user in users])
any_result_2 = any([bool(user[0] == "e") for user in users])
print(all_result_2) #False değer döner
print(any_result_2) #True değer döner
