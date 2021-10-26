import pandas as pd
data=pd.read_csv('C:/Users/mayan/Downloads/datasets/nba.csv')
print(data.head(9))
data.drop(["Team","Weight"],axis=1,inplace=True)
print("New DataBase")
print(data.head(9))