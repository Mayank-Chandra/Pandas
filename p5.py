import pandas as pd
data1={'key':['K0','K1','K2','K3'],
       'Name':['Jai','Princi','Gaurav','Anuj'],
       'Age':[27,22,24,32]}
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
df=pd.DataFrame(data1)
df1=pd.DataFrame(data2)
print(df,"\n\n",df1)
res=pd.merge(df,df1,how='left',on=['key','key1'])
print(res)