import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('input.csv')
salary_data= data.groupby('dept')[['salary']].sum()
print(salary_data)
plt.pie(salary_data['salary'], labels = salary_data.index)
plt.show()



