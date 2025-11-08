import pandas as pd

data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul','Max'],
    'Age' : [21, 20, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Performance_Score':[100,96,98,100,90,94]
}

# Access Single column 

df = pd.DataFrame(data)

print('Names (Single column return series)')
# print(df['Name'])
name = df['Name']
print(name)

# Selecting multiple columns 

sunset = df[["Name", "Salary"]]
print('\nSunset with Name and Salary')
print(sunset)

# Filtering Rows on the bases of single condition 

high_salary = df[df['Salary'] > 2000000]
print('Employees with salary > 2000000')
print(high_salary)

# Filtering Rows on the bases of multiple condition 

filtered = df[(df['Age'] > 25) & (df['Salary'] > 2000000)]
print(f'Employee list Age > 25 + Salary > 2000000')
print(filtered)

# Using OR condition 

filtered_or = df[(df['Age'] > 30) | (df['Perfomance_Score'] > 95)]
print('Employees older then 30 OR performance score > 95')
print(filtered_or)
