import pandas as pd

def DeleteRare(df,col,limit):
   valcounts=df[col].value_counts()
   valreduced=valcounts[valcounts>limit]
   #print("\n valcounts")
   #print(valreduced)
   df_frequent=df[df[col].isin(valreduced.index)]
   return(df_frequent)


testdict={
    'key1': ['a','b','a','a','a','b','a','b'],
    'key2': ['c','c','c','c','d','d','d','d'],
    'num1':[1,1,3,3,3,6,7,8],
    'num2':[40,35,30,25,20,15,10,5]
}

freq_test=pd.DataFrame(testdict)
print(freq_test)

freq_test_rm=DeleteRare(freq_test,'num1',1) #function
print("\nAfter removal of outliers\n")
print(freq_test_rm)




