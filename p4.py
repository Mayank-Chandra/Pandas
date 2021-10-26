import pandas as pd
data=pd.read_csv("C:/Users/mayan/Downloads/datasets/nba.csv")
new=pd.read_csv("C:/Users/mayan/Downloads/datasets/nba.csv")

new['Null Column']=None
print(data.columns.values,'\n',new.columns.values)
print('\n Column number before dropping Null column\n',len(data.dtypes),(len(new.dtypes)))
new.dropna(axis=1,how='all',inplace=True)
print('\ne Column number after dropping Null Column\n',len(data.dtypes),len(new.dtypes))