import pandas as pd

# read data from  CSV file into a dataframe
# df = pd.read_csv("about.csv", encoding="utf-8")   use encoding="lantin1" when file is in old european format
df = pd.read_excel("sample_data.xlsx")

print(df)
