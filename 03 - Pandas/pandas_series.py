import pandas as pd
import numpy as np

pandas_series = pd.Series([1,2,3,4,5,6])


numbers = [1,2,3,4,5,6]
pandas_series_2 = pd.Series(numbers) # Numbers dizisini indexleyip, index numarasıyla beraber yazdırır.

array = pd.Series([1,2,3,'a',"ali",5,6]) # Pandas serileri elemanların veri tipine bakmaz. Seri içerisine istenilen
                                         # veri tipinde değer yazdılabilir.

pandas_series_3 = pd.Series(5,[1,2,3,4,5]) # Index numaraları sırasıyla 1-2-3-4-5 olan 5 tane 5 değeri döndürür.

pandas_series_4 = pd.Series(numbers, ['a','b','c','d','e','f']) # Numbers dizisindeki elemanlara sırasıyla 'a','b',...'f'
                                                        # indexlerini tanımlar.

dict = {"a":10,"b":20,"c":30,"d":40,"e":50}
pandas_series_5 = pd.Series(dict) # Key bilgilerini index olarak alıp value değerleriyle beraber döndürür.

numpy_arr = np.random.randint(10,50,15)
pandas_series_6 = pd.Series(numpy_arr) # Numpy ile oluşturulan diziyi alır ve indexleyip döndürür.

pandas_series_8 = pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f'])
result_2 = pandas_series_8['a']

name = ["Efe","Cengiz","Ali"]
number = [10,20,30]
pandas_series_9 = pd.Series(data=name, index=number)

pandas_series_8 = pd.Series([1,2,3,4,6], index=['a','b','c','d','f'])
result_3 = pandas_series_8['a']

pandas_series_9 = pd.Series([1,3,4,5,6], index=['a','c','d','e','f'])
result_4 = pandas_series_8['a']

contest_result = pandas_series_8 + pandas_series_9 # İlk seride e indexi yok o yüzden çıktıya NaN (Bulunamadı) yazdırır.
                                                   # İkinci seride b indexi yok o yüzden çıktıya NaN (Bulunamadı) yazdırır.







