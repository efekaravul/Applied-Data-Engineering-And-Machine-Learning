import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = numbers[5] # Index numarası 5 olan elemanı döndürür
result = numbers[-1] # Son indexteki elemanı döndürür
result = numbers[0:3] # 0 ve 3. index arasını döndürür. 3. indexteki elemanı yazdırmaz.
result = numbers[3:] # 3. indexten başlayarak son indexteki eleman dahil olucak şekilde değerleri döndürür.
result = numbers[::] # Tüm diziyi yazdırır.
result = numbers[::-1] # Tüm diziyi reverse ederek yazdırır.
result = numbers[::-2] # Reverse şeklinde sürekli bir indexteki elemanı atlayıp bir sonrakini yazdırır.

print(result)

numbers_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
result_2 = numbers_2[2]
result_2 = numbers_2[2,2] # 2 Boyutlu dizi olduğu için ilk dizinin ikinci indexi olan [7,8,9]
                           # dizisinin ikinci indexteki elemanını döndürür.

result_2 = numbers_2[:,2] # Tüm satırların ikinci indexteki elemanlarını döndürür.
result_2 = numbers_2[:,0:2] # Tüm satırların sıfır ve ikinci index arasındaki elemanlarını döndürür.
print(result_2)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans
# arr2[0] = 20
# print(arr2)
# print(arr1) # arr2 de yapılan değişiklik arr1 ide değiştiriyor.

arr3 = arr1.copy()
arr3[0] = 20
print(arr3)
print(arr1) # Burada ise arr1 bir değişikliğe uğramıyor.
