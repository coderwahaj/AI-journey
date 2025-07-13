import pandas as pd
data ={
  "Name":["Wahaj","Aliyan"],
  "Age":[21,16],
  "City":["Lahore","Faisalabad"]
 }

read_data=pd.DataFrame(data)
print(read_data)

#read_data.to_csv("output.csv",index=False)
#read_data.to_excel("output.xlsx",index=False)
#read_data.to_json("output.json",index=False)
