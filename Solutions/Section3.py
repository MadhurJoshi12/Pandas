import pandas as pd
import random 

# Question 8
data ={
    'Name': ['Madhur','Emma','Paul','Alice','Lisa'],
    'Score':[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
}
df = pd.DataFrame(data)
print((df['Score']>80) & (df['Score']<90))

# Question 9
a = df[df['Name'].str.contains('^A',regex =True)]
print(a)

# Question 10
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': ['45', '67', '32', '50']}  # Scores are strings
df = pd.DataFrame(data)
df['Score'] = df['Score'].replace('^[0-4][0-9]$', '50', regex=True)
print(df)


