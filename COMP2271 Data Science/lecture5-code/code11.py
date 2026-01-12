import pandas as pd
 
pddupval = pd.read_csv('DuplDemoRow.csv')
print(pddupval)

print("\nDrop full duplicates")
dropped=pddupval.drop_duplicates()
print(dropped)



