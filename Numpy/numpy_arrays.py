import numpy as np

result = np.array([1,2,3,4,5]) # Verilen değerlerle dizi oluşturur.
print(result)

result_2 = np.arange(10,100,3) # 10 ile 100 arasında artış miktarı 3 olan bir dizi oluşturur
print(result_2)

result_3 = np.zeros(10) # 0 lardan oluşan 10 elemanlı bir dizi oluşturur.
print(result_3)

result_4 = np.ones(10) # 1 lerden oluşan 10 elemanlı bir dizi oluşturur.
print(result_4)

result_5 = np.linspace(0,100,5) # 0 ile 100 arasını 5 eşit parçaya böler
print(result_5)

result_6 = np.random.randint(0,10,3) # 0 ile 10 arasında rastgele 3 tane integer değer üretir
print(result_6)

result_7 = np.random.rand(5) # 0 ve 1 arasında rastgele 5 değer üretir
print(result_7)

np_array = np.arange(50) # 0dan 49a kadar tam sayı değerleriyle dizi oluşturur
np_multi = np_array.reshape(5,10) # yukarıda oluşturulan diziyi 5e 10luk bir matris haline getirir
print(np_multi.sum(axis=1)) # Yukarıda oluşturulan matrisin satırlarının toplamını verir
print(np_multi.sum(axis=0)) # Yukarıda oluşturulan matrisin sütunlarının toplamını verir

np_array_2 = np.random.randint(0,100,20)
np_multi_2 = np_array_2.reshape(5,4)
print(np_multi_2)
print(np_multi_2.sum(axis=1))
print(np_multi_2.sum(axis=0))

np_array_3 = np.random.randint(0,100,20)
print(np_array_3)
np_max = np_array_3.max() # Oluşturulan dizideki en yüksek değeri bulur.
np_min = np_array_3.min() # Oluşturulan dizideki en düşük değeri bulur.
np_mean = np_array_3.mean() # Oluşturulan dizinin ortalamasını bulur.
np_arg_max = np_array_3.argmax() # Oluşturulan dizideki en büyük sayının index numarasını bulur.
np_arg_min = np_array_3.argmin() # Oluşturulan dizideki en küçük sayının index numarasını bulur.
print(np_max)