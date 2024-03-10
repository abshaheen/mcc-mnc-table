import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.mcc-mnc.com/"
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')  

# Create the CSV output file
with open('mcc_mnc_table.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['MCC', 'MNC', 'ISO', 'Country', 'Country Code', 'Network'])

    for row in table.find_all('tr'):
        data = []
        for cell in row.find_all('td'):
            text = cell.get_text().strip()
            data.append(text)

        if data:  # Only process rows with data
            # Do conversions of MCC and MNC to integers here if needed
            csv_writer.writerow(data)
