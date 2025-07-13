import pandas as pd

# Create two sample DataFrames with a common column 'id'
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'age': [34, 23, 28]
})

df2 = pd.DataFrame({
    'id': [4, 5, 6],
    'age': [23, 34, 45]
})

# Inner Join
inner_merged = pd.merge(df1, df2, on='id', how='inner')
print("Inner Join:\n", inner_merged, "\n")

# Outer Join
outer_merged = pd.merge(df1, df2, on='id', how='outer')
print("Outer Join:\n", outer_merged, "\n")

# Left Join
left_merged = pd.merge(df1, df2, on='id', how='left')
print("Left Join:\n", left_merged, "\n")

# Right Join
right_merged = pd.merge(df1, df2, on='id', how='right')
print("Right Join:\n", right_merged, "\n")

# Cross Join
cross_merged = pd.merge(df1, df2, how='cross')
print("Cross Join:\n", cross_merged, "\n")

# Concatenate df1 and df2 vertically (stack rows)
concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(f'Concat : \n{concat}')