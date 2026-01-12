import pandas as pd

def DepTest(df,var1,var2):
  groupvars=df.groupby([var1])
  stored=False
  for key,group in groupvars:
    counts=group[var2].value_counts(normalize=True)  
    print(counts)
    if not stored: 
       #Storing the first distribution
      storedcounts=counts.copy()
      stored=True
    else:
      #Comparing the distribution of the current fragment against the stored one 
      if not storedcounts.equals(counts): 
        return False
  return True


pdvars = pd.read_csv('dependencies.csv')
print(pdvars)

print('\nTesting var1 vs var2')
result=DepTest(pdvars,'var1','var2')
print(result)

print('\nTesting var1 vs var3')
result=DepTest(pdvars,'var1','var3')
print(result)

