# Step 1: Import required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 2: Set the target URL
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

# Step 3: Send a GET request to the URL
req= requests.get(url)
print(req.status_code)

# Step 4: Parse the HTML content if the request was successful
if req.status_code == 200:
    soup=BeautifulSoup(req.text, 'html.parser')
    # Step 5: Extract product names
    productNames = [item.text.strip() for item in soup.find_all('a', class_='title')]
    # Step 6: Extract product prices
    productPrices = [item.text.strip() for item in soup.find_all('h4', class_='price')]
    # Step 7: Extract product descriptions
    productDescriptions = [item.text.strip() for item in soup.find_all('p', class_='description')]
    # Step 8: Extract product reviews
    productReviews = [item.text.strip() for item in soup.find_all('p', class_='review-count float-end')]
    # Step 9: Print the extracted data
    print(productNames)
    print(productPrices)
    print(productDescriptions)
    print(productReviews)
df=pd.DataFrame(
    {
        'Product Name':productNames,
        'Price':productPrices,
        'Description':productDescriptions,
        'Reviews':productReviews
    }
)
print(df)
# Step 10: Save the data to a CSV file
df.to_csv('products.csv', index=False)
print('Data has been saved to products.csv')