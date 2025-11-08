import pandas as pd

data = {
    'Name': ['Madhur','Raja', 'Varun','Elon','Sara'],
    'Age': [21,34,21,53,17],
    'Salary':[12000,5000,8700,4000,1100]
}
df = pd.DataFrame(data)
grouped = df.groupby('Age')['Salary'].sum()
print(grouped)


# Grouping multiple columns 
MultiGrouped = df.groupby(['Age','Name'])['Salary'].sum()
print(MultiGrouped)


'''
**Some common aggregation function**
sum()
mean()
count()------> It will count non NAN values
min()
max()
std()
'''