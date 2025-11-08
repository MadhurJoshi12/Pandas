# Type of missing data 
# NaN (Not a number)
# None(for object data types)

# pd.isnull()
# True - value is not present(None or NaN) 
# False - value is present 
import pandas as pd
data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul',None],
    'Age' : [21, None, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,None,94]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())



# dropna()
# df.dropna(axis = 1, inplace=True)     This will remove column
# df.dropna(inplace=True)
# df.dropna(inplace=True)               This will act as axis = 0
# print(df)



#fillna()
# df.fillna("Not Found", inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)
