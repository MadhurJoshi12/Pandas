import pandas as pd

data = {
    "Name":["Lisa","Elsa","Elon","Paul"],
    "Score":[81,72,92,72]
}
df = pd.DataFrame(data)
print(df)
print("")

# Replace all 72 to 86
df['Score'] = df["Score"].replace(72,86)
print(df)

var = pd.read_csv("output.csv")
print(var)
print("")
var["City"] = var["City"].replace("florida", "Vegas")
print(var)

var['Age'] = var["Age"].replace([21,27,20],50)
print(var)
