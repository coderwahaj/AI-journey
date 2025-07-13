import pandas as pd

data = {
    "Name": [
        "Ali", "Zara", "Hamza", "Sara", "Usman",
        "Ayesha", "Bilal", "Mehwish", "Fahad", "Hina"
    ],
    "Age": [31, 30, 28, 26, 35, 29, 32, 27, 31, 24],
    "Salary": [34000, 62000, 58000, 54000, 67000, 60000, 61000, 55000, 59000, 51000],
    "Performance Score": [7.5, 8.2, 6.9, 7.0, 8.5, 7.8, 7.6, 6.5, 7.9, 7.1]
}


df = pd.DataFrame(data)
print(df)
#If you're unsure about the exact column names:
print(f'Column Names : {df.columns.tolist()}')

#Adding column
#Two Ways
#1-Using assignment
df['Bonus'] = df['Salary'] * 0.1
print(df)
#2-Using Insert method to enter in the precise location
df.insert(0,'EmployeeID',[1,2,3,4,5,6,7,8,9,10])
print(df)

#Updating 
#df.loc[row_index,'Column Name']=new value
# df.loc[0,'Salary']=55000
# print(df)

#Updating all data of specific column
# df['Salary']=df['Salary']*1.05
# print(df)

#Removing columns
print( 'Data After Removing the column : ')
# Dropping the 'Bonus' column as it is no longer needed for further analysis
#To remove multiple columns using comma separated column names
df.drop(columns=['Bonus'], inplace=True)
print(df)

#Sort 
#ascending =True/False
df.sort_values(by=['Salary','Age'],ascending=[True,False],inplace=True)
print(f'After sorting Salary in ascending Order :\n {df}')

# Calculate mean, min, max, and sum of Salary
salary_list = data["Salary"]
print(f"Salary Mean: {sum(salary_list)/len(salary_list)}")
print(f"Salary Min: {min(salary_list)}")
print(f"Salary Max: {max(salary_list)}")
print(f"Salary Sum: {sum(salary_list)}")
print(f"Salary Std: {pd.Series(salary_list).std()}")
print(f"Salary Count: {len(salary_list)}")
#groupby 
grouped =df.groupby('Age')['Salary'].mean()
print(grouped)