import pandas as pd

# Question 1
df = pd.read_csv('student.csv')
print(df)

# Question 2
# Save the first 10 rows to a new CSV file
df.head(10).to_csv('top_students.csv', index=False)

# Question 3
# Load all sheets into a dictionary
all_sheets = pd.read_excel('data.xlsx', sheet_name=None)
print(all_sheets.keys())
    