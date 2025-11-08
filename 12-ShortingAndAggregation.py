import pandas as pd
# Shorting data in one column 
data = {
    'Name': ['Madhur','Raja', 'Varun'],
    'Age': [28,34,22],
    'Salary':[10000,5000,8000]
}
df = pd.DataFrame(data)
# df.sort_values(by='Age', ascending=False, inplace=True)    #Here ascending=False means short in decending order
# print(df)                                                   #And inplace= True means change the original

# Shorting data in multiple columns 
# df.sort_values(by=['Age','Salary'], ascending=[True,False], inplace=True)
# print(df)



# Aggregatating Data 
#Summary statistics
avg_salary = df['Salary'].mean()
print(avg_salary)
