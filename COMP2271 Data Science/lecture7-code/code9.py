import pandas as pd

dict1={
'numbers':[1,2,3,4],
'connect':[1,1,2,7]
}

dict2={
'connect':[2,2,1,8],
'letters':['a','b','c','d']
}

#Value 4 of 'connect' column is missing in df2
#Value 8 of 'connect column is missing in df1
df1=pd.DataFrame(dict1)
print(df1)
df2=pd.DataFrame(dict2)
print(df2)

#Missing values ignored
df=pd.merge(df1,df2)
print(df)

#Missing values included in dummy rows.
#This is one more source of occurrence 
#of missing values in a DataFrame 
dfouter=pd.merge(df1,df2,how='outer')
print(dfouter)

