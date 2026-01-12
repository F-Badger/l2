import pandas as pd

def OutliersBound(sr):
  quartiles=sr.quantile([0.25,0.5,0.75])
  iqr=quartiles[0.75]-quartiles[0.25]
  lb=quartiles[0.25]-1.5*iqr
  ub=quartiles[0.75]+1.5*iqr
  return (lb,ub)

qs=pd.Series([1,2,300,400,500,600,700,800,900,1000,1100,12000,13000])
bounds=OutliersBound(qs)
print('\nThe outliers bounds are:')
print(bounds)


