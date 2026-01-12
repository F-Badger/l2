import pandas as pd
 

pddupval = pd.read_csv('DuplDemoRow.csv')
print(pddupval)

print('\nDiscover full duplicates')
print(pddupval.duplicated())

print('\nDiscover duplicates for col1 only')
print(pddupval.duplicated(subset=['col1']))





