import pandas as pd
data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul',None],
    'Age' : [21, None, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,None,94]
}
df = pd.DataFrame(data)
# Question 11
print(df.isnull().sum(axis=1).to_string(index=False))
        
# Question 12
df.dropna(axis=1,inplace=True)
print(df)

# Question 13
data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul',None],
    'Age' : [21, None, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,None,94]
}
df = pd.DataFrame(data)

# Fill missing Age with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)

# Question 14
df['Perfomance_Score'].fillna(method='ffill', inplace=True)
print(df)

# Question 15
import pandas as pd

data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul',None],
    'Age' : [21, None, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,None,94]}
df = pd.DataFrame(data)
df['Perfomance_Score'] = df['Perfomance_Score'].interpolate(method='linear')
print(df)
