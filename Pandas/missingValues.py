#Nan(Not a Number)
#None(for object Data Types)

#isnull()-True,False


import pandas as pd

data = {
    "Name": [
        "Ali", None, "Hamza", None, "Usman",
        "Ayesha", None, "Mehwish", "Fahad", "Hina"
    ],
    "Age": [31, None, 28, 26, 35, 29, 32, 27, 31, 24],
    "Salary": [34000, None, 58000, None, 67000, 60000, 61000, 55000, 59000, 51000],
    "Performance Score": [7.5, None, 6.9, 7.0, 8.5, 7.8, 7.6, 6.5, 7.9, 7.1]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
# To drop missing values 
#For rows axis=0,For Columns axis=1 
# df.dropna(axis=0,inplace=True)

# print(df)

#To Fill missing values with default value
# df.fillna(0,inplace=True)

# print(df)

df['Name'].fillna('XYZ',inplace=True)

df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)

df['Performance Score'].fillna(df['Performance Score'].mean(),inplace=True)
print(df)

