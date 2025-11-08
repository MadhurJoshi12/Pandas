import pandas as pd

data = {
    "Name": ['Madhur','Emma','Elsa'],
    "Age" : [21, 27, 20],
    "City": ['Berlin','florida','paris']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
