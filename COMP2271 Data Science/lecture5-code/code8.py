import pandas as pd

pdtemp = pd.read_csv('misstemp.csv')
print(pdtemp)

#Filling all the gaps with fill forward method
print("\nFill Forward:")
fwtemp=pdtemp.fillna(method='ffill')
print(fwtemp)

#An existing entry used for filling
#a missing missing in the row immediately next to it
print("\nFill Forward with limit 1:")
fwlimit=pdtemp.fillna(method='ffill',limit=1)
print(fwlimit)

