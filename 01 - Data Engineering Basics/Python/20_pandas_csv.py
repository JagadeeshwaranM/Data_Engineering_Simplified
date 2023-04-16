import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('input.csv')
print(type(data))
print (data)
print(data[0:5]['salary'])
print (data.loc[:,['salary','name']])
print (data.loc[[1,3,5],['salary','name']])
print (data.loc[2:6,['salary','name']])




