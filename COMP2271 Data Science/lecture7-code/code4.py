import pandas as pd

pdrepeat=pd.read_csv('examsrepeat.csv')
print(pdrepeat)
pdsummary=pdrepeat.groupby(['id']).max()
print("\nAfter removal of duplicates:")
print(pdsummary)
print('\nType=',type(pdsummary))
print('Index=',pdsummary.index)
print('Columns=',pdsummary.columns)


