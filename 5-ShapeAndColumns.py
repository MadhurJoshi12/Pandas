'''
1- How big is your dataset?
2- What are the names of columns
'''
import pandas as pd

data = {
    'Name': ['Madhur','Lisa','Emma','Kylie','Paul','Max'],
    'Age' : [21, 20, 27, 32, 36, 41],
    'Salary':[10000000, 4000000, 5000000, 9000000,3000000,2000000],
    'Perfomance Score':[100,96,98,100,90,94]
}
df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')
