'''
1- Understand the data set
2- Identify the problems
3- Plan next steps
'''
import pandas as pd
df = pd.read_excel("sample_data.xlsx")

print('Display 2 rows of first')
# print(df.head())    *By default it will 5 rows
print(df.head(2))

print('Display 2 rows of last')
# print(df.tail())    *By default it will 5 rows
print(df.tail(2))
