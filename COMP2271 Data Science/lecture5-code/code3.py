import pandas as pd

pdmarks = pd.read_csv('missvalues.csv')
print(pdmarks)
print("\nDrop rows with at least one missing element:")
pdfullrows=pdmarks.dropna()
print(pdfullrows)
print("\nDrop columns with at least one missing element:")
pdfullcolumns=pdmarks.dropna(axis=1)
print(pdfullcolumns)






