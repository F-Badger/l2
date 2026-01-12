import pandas as pd
import numpy as np

def OutliersBound(sr):
  quartiles=sr.quantile([0.25,0.5,0.75])
  iqr=quartiles[0.75]-quartiles[0.25]
  lb=quartiles[0.25]-1.5*iqr
  ub=quartiles[0.75]+1.5*iqr
  return (lb,ub)


def OutliersRemStat(df,col):
  (lb,ub)=OutliersBound(df[col])
  print('\nThe outliers bounds are:')
  print(lb,ub)
  
  #Patterns for filtering upper and lower bounds
  lbpatt=df[col]>=lb
  ubpatt=df[col]<=ub
  
  #Their elementwise conjunction
  genpatt=np.logical_and(lbpatt,ubpatt)
  df_outrem=df[genpatt]
  return df_outrem

pdsalaries = pd.read_csv('salaryoutliers.csv')
print(pdsalaries)

salaries_cleaned=OutliersRemStat(pdsalaries,'salary')
print('\nAfter removal of outliers:')
print(salaries_cleaned)




