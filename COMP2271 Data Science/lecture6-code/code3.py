import pandas as pd

testdict={
    'key1': ['a','b','a','a','a','b','a','b'],
    'key2': ['c','c','c','c','d','d','d','d'],
    'num1':[1,1,3,3,3,6,7,8],
    'num2':[40,35,30,25,20,15,10,5]

}
freq_test=pd.DataFrame(testdict)
print(freq_test)

print("\nApply value_counts():")
limit=1
valcounts=freq_test['num1'].value_counts()
print(valcounts)

print("\nFiltering out values with low counts:")
valreduced=valcounts[valcounts>limit]
print(valreduced)





