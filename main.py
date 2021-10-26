import pandas as pd
data={'name':['Jai','Princi','Gaurav','Anuj'],'Height':[5.1,6.2,5.1,5.2],'Qualification':['Msc','MA','Msc','Msc']}
df=pd.DataFrame(data)
address=['Delhi','Mumbai','Ayodhya','Modinagar']
df['Address']=address
print(df)