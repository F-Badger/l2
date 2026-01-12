import pandas as pd

pdmv = pd.read_csv('missvalues.csv')
print(pdmv)

#Column pattern
misscolumn=pdmv['col2'].isnull()
#Check a specific value
print("\n col 2, row 1: ",misscolumn[1]) 

#Row pattern
missrow=pdmv.loc[1].isnull()
#Check a specific value
print("\n row 1, col 2: ",missrow[1]) 





