import pandas as pd

#Read data from CSV/xlsx/json file into dataframe

read_data=pd.read_json("sample_Data.json",encoding="latin1")

print("Display the First 10 rows : ")
print(read_data.head(10))

print("Display the Last 10 rows : ")
print(read_data.tail(10))
