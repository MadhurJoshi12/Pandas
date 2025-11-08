import pandas as pd

data ={
    'Name': ['Madhur','Emma','Paul','Lisa','Raj'],
    'Score': [100,92,87,85,71],
    'Age': [23,26,28,24,29]
}
# Question 4
df = pd.DataFrame(data)
print(df[['Name','Score']])

# Question 5
a = df[df['Age']>25]
print(a)

# Question 6
c = df.loc[df['Name'] == 'Raj', 'Score']
print(c)

# Question 7
k = df.iloc[-3:]
print(k)

