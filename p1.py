import pandas as pd
data={'Name':['Mayank','Harsh','Ayush','Homie'],'Class':[12,12,12,11],'Section':['A','B','C','D']}
df=pd.DataFrame(data)
df2=df.assign(Rollno=[12,33,21,15])
print(df2)