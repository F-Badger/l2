import pandas as pd

pdmarks = pd.read_csv('marksmissing.csv')
print(pdmarks)
 
pdmarksfull=pdmarks.fillna(0)
print("\nFill all the missing values with 0")
print(pdmarksfull)

