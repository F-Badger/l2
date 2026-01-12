import pandas as pd

dict1={
'numbers':[1,2,3],
'connect':[1,1,2]
}

dict2={
'connect':[2,2,1],
'letters':['a','b','c']
}

df1=pd.DataFrame(dict1)
print(df1)
df2=pd.DataFrame(dict2)
print(df2)

df=pd.merge(df1,df2)
print(df)

