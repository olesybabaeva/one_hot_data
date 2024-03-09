import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmi': lst})
data.head()

unik = data['whoAmi'].unique()
one_hot_data = pd.DataFrame()

for new in unik:
  one_hot_data[new] = (data['whoAmi'] == new).astype(int)
one_hot_data.head()
