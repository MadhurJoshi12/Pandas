# Adding column 
import pandas as pd

data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul','Max'],
    'Age' : [21, 20, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance_Score':[100,96,98,100,90,94]
}

df = pd.DataFrame(data)
print(df)

# Method 1
df["Bonus"] = df['Salary'] * 0.1
print(df)

# Method 2 (Using insert)
# df.insert(location, "Coluumn name", some data)
df.insert(0, "Employee ID", [1,2,3,4,5,6])
print(df)

# Updating Value 

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data, index=['Column1', 'Column2', 'Column3'])
# Using loc
print(df.loc['Column1'])  # Access row by label
print(df.loc['Column1', 'A'])  # Access specific cell by row label and column label
print(df.loc['Column1':'Column2', 'A'])  # Slice rows and columns by labels

# Using iloc 
# df.iloc[row_index, column_index]

# Using iloc
print(df.iloc[0])  # Access the first row (position 0)
print(df.iloc[0, 1])  # Access the cell at the first row and second column (position 0,1)
print(df.iloc[0:2, 0])  # Slice rows by position and select a specific column by position


# increasing salary by 5% 
df['Salary'] = df['Salary'] * 1.05
print(df)

# Removing Column 
# df.drop(columns= ["ColumnName", "ColumnName", "ColumnName"...], inplace=True) means change the original data and inplace= False means make a copy then update
df.drop(columns= ["Employee ID"], inplace=True)
print(df)
