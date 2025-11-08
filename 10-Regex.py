import pandas as pd

# Finding Row with Regex 
data ={
    'Name':['Madhur','Raj','Rahul','Aman','Raja'],
    'Score':[86,79,92,80,75]}
df= pd.DataFrame(data)


# Finding names starting with Ra 
result = df[df['Name'].str.contains('^Ra', regex=True)]
print(result)


# Replacing using Regex 
'''Replace any name starting with Ra---->mj'''
df['Name'] = df['Name'].replace(to_replace='^Ra*', value='mj',regex=True)
print(df)


# Extracting Pattern
email = pd.DataFrame({
    'Email':['madhur123@gmail.com','test99@yahoo.com']
})
email['Usename'] = email['Email'].str.extract(r'(^\w+)')
print(email)


# Splitting text with regex
fr = pd.DataFrame({'Data': ['Name: Madhur | Score: 86']})
print(fr)
fr[["Key1","key2"]] = fr['Data'].str.split(r'\s*\|\s*', expand=True)
print(fr)


# Pro Tips
'''
^word   ------------------->starts with word
word$   ------------------->ends with word
*       ------------------->any number of characters
[0,9]   ------------------->digits
[A-Za-z]------------------->letters
''' 