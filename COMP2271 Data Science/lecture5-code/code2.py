import pandas as pd
 
pdsalary = pd.read_csv('missingsalary.csv')
print(pdsalary)
#By default, the function mean ignores missing values
print("\nMean per row:")
means=pdsalary[pdsalary.columns[1:]].mean(1)
print(means)


