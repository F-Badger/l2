import pandas as pd

def DeleteRareMapped(df,col,limit,mf):
  #Mapping values to their clusters
  map_column=df[col].map(mf)
  print("\nMap_column")
  print(map_column)

  #Computing frequencies for the clusters
  valcounts=map_column.value_counts()

  #Removal the rare clusters
  valreduced=valcounts[valcounts>limit]

  #Filtering the input dataset
  df_frequent=df[map_column.isin(valreduced.index)]
  return(df_frequent)

def MarkstoClasses(mark):
  if mark>=70:
    return '1'
  elif mark in range(60,70):
    return '2:1'
  elif mark in range(50,60):
    return '2:2'
  elif mark in range(40,50):
    return '3'
  else: 
    return 'fail'

pdmarks = pd.read_csv('student_marks.csv')
print(pdmarks)
pdmarks_norare=DeleteRareMapped(pdmarks,'Maths',1,MarkstoClasses)
print("\nAfter removal:")
print(pdmarks_norare)

