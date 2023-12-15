import pandas as pd
file = pd.read_csv('data.txt')
filltered_file = file[file['Country'] == 'Oman']
vecakais = filltered_file['Founded'].min()
print(vecakais)

#kaut kas nestrada