import pandas as pd
# Customer DataFrame 
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Madhur','Ramesh','Gukesh']
})
# Order Dataframe 
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

# Merge 
df_merge = pd.merge(df_customers, df_orders, on="CustomerID", how='inner')
print(df_merge)



# Concatenation/Joining DataFrame
df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Gopal','Raju']
})

df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Madhur','Mohan']
})

df_concatenate = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concatenate)
# By default it is vertical (axis =0) or you can say merge rowwise

df_concatenate = pd.concat([df_Region1, df_Region2], axis=1,ignore_index=True)
print(df_concatenate)
# Now this is Horizontally concatenate (axis=1) or you can say merge columnwise 
