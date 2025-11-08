import pandas as pd

data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul',None],
    'Age' : [21, None, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,None,94]
}
df = pd.DataFrame(data)

# Question 16
mean_score = df['Perfomance_Score'].mean()
print(mean_score)
medium_score = df['Perfomance_Score'].median()
print(medium_score)
std_score = df['Perfomance_Score'].std()
print(std_score)

# Question 17
max_age = df['Age'].max()
print(max_age)
mini_age = df['Age'].min()
print(mini_age)


# Question 18
grouped = df.groupby('Age')['Perfomance_Score'].mean()
print(grouped)
