import pandas as pd

pdrepeat=pd.read_csv('examsrepeat.csv')
print(pdrepeat)
print("\nAfter removal of duplicates:")
pdsummary2=pdrepeat.groupby(lambda ind: pdrepeat['id'][ind]).max()
print(pdsummary2)
print("\nThen reset index:")
pdsummary3=pdsummary2.reset_index(drop=True)
print(pdsummary3)

