import pandas as pd
import numpy as np
data = [0,1,2,3,4,5]
list = [['Alex',10],['Bob',12],['Clarke',13]]
dict = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df_list = pd.DataFrame(list,columns=['Name','Age'])
df_dict = pd.DataFrame(dict)
df_series = pd.Series(np.random.randn(4))
print(df)
print(df_list)
print(df_dict)
print(df_series)
print(df_list.head(2))
print(df_dict.tail(2))