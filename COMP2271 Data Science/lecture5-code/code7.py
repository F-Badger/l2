import pandas as pd

pdsalary = pd.read_csv('missingsalary.csv')
print(pdsalary)

print("\nAverage per row:")
#IDs omitted for the purpose of means computation
#By default, the function mean() ignores missing values
means=pdsalary[pdsalary.columns[1:]].mean(1)
print(means)

#Filling the missing values 
print("\nFilling the missing values with averages")
for i in pdsalary.index:
  pdsalary.loc[i]=pdsalary.loc[i].fillna(means[i])
print(pdsalary)
  

