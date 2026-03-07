import pandas as pd
# Load the CSV file into a DataFrame
data = pd.read_csv('data.csv')
# Display the first few rows of the DataFrame
print(data.head())
# Get summary statistics of the DataFrame
print(data.describe())
# Check for missing values
print(data.isnull().sum())
import requests
# Download the CSV file from a URL
url = 'https://example.com/data.csv'
response = requests.get(url)
# Save the content to a local file
with open('downloaded_data.csv', 'wb') as file:
    file.write(response.content)
# Load the downloaded CSV file into a DataFrame
downloaded_data = pd.read_csv('downloaded_data.csv')
# Display the first few rows of the downloaded DataFrame
print(downloaded_data.head())
