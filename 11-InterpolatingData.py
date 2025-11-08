import pandas as pd
# Interpolating Data
'''
1 - preserve data integrity 
2 - smooth trends
3 - avoid data loss
''' 
# methods = linear, polynomial, time 

data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df = pd.DataFrame(data) 
print("Before interpolation")
print(df)

df['Value'] = df["Value"].interpolate(method="linear")
print("After interpolation")
print(df)

#By Default interpolatation is linear
# data = {
#     'Day': [1, 2, 3, 4, 5],
#     'Score': [10, None, 30, None, 50]
# }
# df = pd.DataFrame(data)
# print("Original:")
# print(df.interpolate())           Linear interpolitation


# POLYNOMIAL METHOD
# data = {
#     'x': [0, 1, 2, 3, 4, 5],
#     'y': [0, None, 8, None, 64, 125]}  # cubic-like growth
# df = pd.DataFrame(data)
# print(df.interpolate(method='polynomial', order=3))


# TIME METHOD 
# dates = pd.date_range("2023-01-01", periods=5)
# data = {'Temperature': [30, None, 34, None, 40]}
# df = pd.DataFrame(data, index=dates)

# print(df.interpolate(method='time'))
