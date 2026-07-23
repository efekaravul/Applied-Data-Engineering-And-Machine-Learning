import numpy as np

#1

arr1 = np.array([1,2,3,4,5])

#2

arr2 = np.arange(5,15)

#3

arr3 = np.arange(50,100,5)

#4

arr4 = np.zeros(10)

#5

arr5 = np.ones(10)

#6

arr6 = np.linspace(0,100,5)

#7

arr7 = np.random.randint(10,30,5)

#8

arr8 = np.random.randn(10)

#9

arr9 = np.random.randint(10,50,15).reshape(3,5)

#10

arr10 = np.array([10,11,12,13,14,15,16,17,18,19,20])
result = arr10[0:3]

#11

arr11 = np.random.randint(10,50,15)
result = arr11[:-1]

#12

arr12 = np.random.randint(10,50,15).reshape(3,5)
result = arr12[:,1]

#13

arr13 = np.random.randint(10,50,15).reshape(3,5)
result = arr13[2,3]

#14

arr14 = np.random.randint(10,50,15).reshape(3,5)
result = arr14[1,:]

#15

arr15 = np.random.randint(10,50,15).reshape(3,5)
result15 = arr15 ** 2

#16

arr16 = np.random.randint(10,50,15).reshape(3,5)
ciftler = arr16[arr16 % 2 == 0]
pozitif_ciftler = ciftler[ciftler > 0]
print(pozitif_ciftler)


