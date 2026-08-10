import numpy as np

arr1 = np.random.randint(10,100,10)
arr2 = np.random.randint(10,100,10)

arr3 = arr2 + arr1 # İki dizinin elemanlarının toplamını verir.
arr3 = arr2 + 10 # arr2 nin değerlerine 10 ekler.
arr3 = arr2 - 10 # arr2 nin değerlerinden 10 çıkarır.
arr3 = arr1 * arr2 # arr1 ve arr2 nin elemanlarını çarpar.
arr3 = np.sqrt(arr2) # arr2 nin tüm değerlerinin karekökünü alır.
arr3 = np.sin(arr3) # arr2 nin tüm değerlerinin sin değerlerini döndürür.
arr3 = np.cos(arr3) # arr2 nin tüm değerlerinin cos değerlerini döndürür.
arr3 = np.log(arr2) # arr2 nin tüm değerlerinin log değerlerini döndürür.

print(arr1)
print(arr2)
print(arr3)

arr4 = np.random.randint(10,100,10)
arr5 = np.random.randint(10,100,10)

marr = arr4.reshape(2,5)
marr2 = arr5.reshape(2,5)

print(marr)
print(marr2)

vertical_arr = np.vstack((marr,marr2)) # marr ve marr2 dikey olarak birleştirir.
horizantal_arr = np.hstack((marr,marr2)) # marr ve marr2 yatay olarak birleştirir.
print(vertical_arr)
print(horizantal_arr)

arr6 = np.random.randint(10,100,10)
result = arr6 >= 5 # arr6 da bulunan değerlerin beşten büyük olup olmadığını kontrol edip bool türünde değer yollar.
result2 = arr6 % 2 == 0 # arr6 da bulunan değerlerin mod ikisinin 0 a eşit olup olmadığını kontrol edip bool türünde değer yollar.
print(result)
print(result2)
print(arr6[result2]) # arr6 daki result2 koşulunu sağlayan değerleri dizi halinde döndürür.