import pandas as pd

# Question 22
data ={
    'Name' : ['Madhur','Emma','Elon','Lisa','Paul','Tony'],
    'y': [0, None, 8, None, 64, 125]}
df = pd.DataFrame(data)
print(df.interpolate(method='polynomial', order = 3))

# Question 23
df = pd.DataFrame({
    'Phone': ['(123) 456-7890', '+1-800-555-0199', '555.0123', '123 456 7890', '0044 20 7946 0958']})

df['Phone'] = df['Phone'].str.replace(r'\D', '', regex=True)
print(df)


# Question 24
df = pd.DataFrame({
    'Address': ['New York | NY', 'Los Angeles | CA', 'Chicago | IL', 'Houston | TX']})

df[['City', 'State']] = df['Address'].str.split('|', expand=True)
df['City'] = df['City'].str.strip()
df['State'] = df['State'].str.strip()
print(df)