import requests
from bs4 import BeautifulSoup
import csv

url = 'https://stopcorona.tn.gov.in/archive/'
list = []
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
urls = soup.find('div', attrs={"class" : "col-md-12 col-sm-12 col-xs-12"})
atags = urls.find_all('a')
for atag in atags:
    link = atag['href'].replace('"', '')
    title = atag.get_text().strip().replace(' ', '_').replace(',', '')
    list.append([title, link])
    with open('results.csv', 'w', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(list)
        print('file downloaded:..')

    

