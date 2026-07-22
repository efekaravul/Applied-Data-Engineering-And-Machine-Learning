def kareAl(a):
    return a ** 2

sonuc = kareAl(5)
print(sonuc)

sonuc_2 = (lambda x: x ** 2)(3)
print(sonuc_2)

sonuc_3 = lambda m,n,k: m + n + k
sonuc_4 = sonuc_3(4, 5, 6)
print(sonuc_4)

def my_func(n):
    return lambda x: x * n

sonuc_5 = my_func(5) #sonuc_5 myFuncta n değerini 5 olarak atadık
sonuc_6 = sonuc_5(6) #sonuc_6 da sonuc_5 e 6 değeri atadık yani lambda değeri atamış olduk.
print(sonuc_6)