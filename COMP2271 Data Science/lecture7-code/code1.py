import pandas as pd

testdict={
                'key1': ['a','b','a','a','a','b','a','b'],
                'key2': ['c','c','c','c','d','d','d','d'],
                'num1':[1,2,3,4,5,6,7,8],
                'num2':[40,35,30,25,20,15,10,5]
}

pdtest=pd.DataFrame(testdict)
print(pdtest)

#pdtest is divided into two fragments 
#one fragment includes rows with 'key1'='a'
#the other rows with 'key1'='b'
pdgroups1=pdtest.groupby(['key1'])
print(pdgroups1)
print(type(pdgroups1))

