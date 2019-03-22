import pandas as pd

data = pd.read_csv('CRDC2013_14.csv')

print(data[['JJ','SCH_STATUS_MAGNET']].head())
print("JJ value counts:",data['JJ'].value_counts())
print("SCH_STATUS_MAGNET value counts:",data['SCH_STATUS_MAGNET'].value_counts())

print(pd.pivot_table(data, values=['TOT_ENR_M','TOT_ENR_F'], index='JJ', aggfunc='sum'))

print(pd.pivot_table(data, values=['TOT_ENR_M','TOT_ENR_F'], index='SCH_STATUS_MAGNET', aggfunc='sum'))
