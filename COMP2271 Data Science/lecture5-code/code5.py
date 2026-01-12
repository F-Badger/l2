import pandas as pd

pdmarks = pd.read_csv('marksmissing.csv')
print(pdmarks)
print("\nfilling all the missing values with zeroes")
pdmarksfull=pdmarks.fillna(0)
print(pdmarksfull)


