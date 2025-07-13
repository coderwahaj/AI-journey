import pandas as pd

#Read data from CSV/xlsx/json file into dataframe
# read_data=pd.read_csv("sales_data_sample.csv",encoding="latin1")

# read_data=pd.read_excel("SampleSuperstore.xlsx",encoding="latin1")

#read_data=pd.read_json("sample_Data.json",encoding="latin1")
#print(read_data)

# If we want to read data from Google cloud store then use 
# gcsfs


#import pandas as pd

# Path to your large CSV file
file_path = 'sales_data_sample.csv'

# Define chunk size (number of rows per chunk)
chunk_size = 100  # adjust this as needed

# Create a generator for chunks
chunk_iter = pd.read_csv(file_path, chunksize=chunk_size,encoding="latin1")

# Example: Process each chunk
for i, chunk in enumerate(chunk_iter):
    print(f"Processing chunk {i + 1}")
    print(chunk.head())  # or do any processing you want here
