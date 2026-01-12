import pandas as pd
 
pddupval = pd.read_csv('DuplDemoRow.csv')
print(pddupval)
print('\nDrop duplicates for col1')
      
print('\nKeep the first entry')
dropped1=pddupval.drop_duplicates(subset=['col1'])
print(dropped1)

print('\nKeep the last entry')
dropped2=pddupval.drop_duplicates(subset=['col1'], keep='last')
print(dropped2)











