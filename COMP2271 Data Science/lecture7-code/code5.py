import pandas as pd


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
    return 'Fail'

pdmarks = pd.read_csv('student_marks.csv')
print(pdmarks)
groupmarks=pdmarks.groupby(lambda ind: MarkstoClasses(pdmarks['Maths'][ind]))
print(groupmarks)

for key,group in groupmarks:
  print("\nKEY =",key)
  print(group)
  
  