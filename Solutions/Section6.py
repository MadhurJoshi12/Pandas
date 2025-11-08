import pandas as pd

data ={
    'Name': ['Madhur','Elon','Justin','Emma','Raj'],}
df = pd.DataFrame(data)

# Question 19
df['Name'] = df['Name'].replace(to_replace='Raj', value='Rohan',regex=True)
print(df)

# Question 20
df = pd.DataFrame({
    'Name': ['John123', 'An@#na', 'Mi-ke!', 'O\'Connor', '123Tom']})
df['Name'] = df['Name'].str.replace('[^A-Za-z]', '', regex=True)
print(df)

# Question 21
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Mike', 'OConnor', 'Tom']})
df['ShortName'] = df['Name'].str[0:3]
print(df)
