import pandas as pd
import numpy as np

pd_1 = pd.read_csv("../Data/7-concat_data1.csv")
pd_2 = pd.read_csv("../Data/7-concat_data2.csv")
print(pd_1)
print(pd_2)

pd_concat = pd.concat([pd_1, pd_2], ignore_index=True) # Concat dataframeleri birleştirir. ignore_index = True yaparak
print(pd_concat)                                            # ikinci dataframeden 0 dan başlayarak gelen index numaralarını
                                                            # ilk dataframein index numaralarının devamıymış gibi yazdırırız
                                                            

