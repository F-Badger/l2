import pandas as pd

testdict={
                'key1': ['a','b','a','a','a','b','a','b'],
                'key2': ['c','c','c','c','d','d','d','d'],
                'num1':[1,2,3,4,5,6,7,8],
                'num2':[40,35,30,25,20,15,10,5]
}

pdtest=pd.DataFrame(testdict)
print(pdtest)

pdgroups1=pdtest.groupby(['key1'])
print(pdgroups1)

print("\nGet group a:")
subframe=pdgroups1.get_group('a')
print(subframe)

