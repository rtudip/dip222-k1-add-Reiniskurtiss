import pandas as pd
s = 0
file = pd.read_csv('data.txt')
for index, row  in  file.iterrows():
    if row ['Country'] == 'Latvia':
        s = s+1
print(s)