#Read data from CSV/xlsx/json file into dataframe

# read_data=pd.read_json("sample_Data.json",encoding="latin1")

# print("Display the Info of data set : ")
# print(read_data.info())
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
# 1-columns,rows
# 2-what type of data?
# 3-missing data

# info()->method

# 1-no of columns and rows
# 2-column name
# 3- int64 float64 object
# 4-non null count 
# 5-memory usage of data frame
df = pd.DataFrame(data)
print(df.info())
print(df)

#Summarize data and to analyze it 
print("Discriptive Statistics :")
print(df.describe())
#No of rows and columns of Data
print(f'Shape of Data Frame :{df.shape}')
#Column Names of Data
print(f'Column Names of Data Frame :{df.columns}')
#Rename the Column
df.rename(columns={'Salary':'EmployeeSalary'},inplace=True)
print(df)
#1-Selecting specific Column return a Series or DataFrame of multiple columns
print("Display a single column(Name) return a series : ")
name=df['Name']
print(name)
print("Display multiple columns(Name and Salary) returns a dataframe : ")
subset=df[['Name','EmployeeSalary']]
print(subset)

#2-Filter rows based on Boolean Indexing
print(df)
print("Filter employees salary > 50000 and age >30: ")
filter = df[(df['EmployeeSalary'] > 50000) & (df['Age'] > 30)]
print(filter)
print("Filter employees salary > 50000 OR age >30: ")
filter = df[(df['EmployeeSalary'] > 50000) | (df['Age'] > 30)]
print(filter)