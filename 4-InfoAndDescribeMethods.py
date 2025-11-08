'''
Problems:-
1-Clomns, row?
2-What type of?
3-Missing data?
'''
import pandas as pd
# Info Method 
df = pd.read_excel("sample_data.xlsx")
print(df.info()) 


# Describe Method 
data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul','Max'],
    'Age' : [21, 20, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance Score':[100,96,98,100,90,94]
}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Descriptive Statistics")
print(df.describe())
