import pandas as pd
 
pdmissing = pd.read_csv('missingrow.csv')
print(pdmissing)
print("\nDrop rows with all values missing:")
pdnoallmissing=pdmissing.dropna(how='all')
print(pdnoallmissing)







