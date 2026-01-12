import pandas as pd

qs=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13])
quartiles=qs.quantile([0.25,0.5,0.75])
print('The quartiles belong to the data points')
print(quartiles)
print('Q1=',quartiles[0.25],'Q3=',quartiles[0.75])



