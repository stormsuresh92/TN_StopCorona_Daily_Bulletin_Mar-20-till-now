import requests
from bs4 import BeautifulSoup

url = 'https://stopcorona.tn.gov.in/archive/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
urls = soup.find('div', attrs={"class" : "col-md-12 col-sm-12 col-xs-12"})
atags = urls.find_all('a')
for atag in atags:
    link = atag['href'].replace('"', '')
    title = atag.get_text().strip().replace(' ', '_').replace(',', '')
    try:
        with open(title + '.pdf', 'wb') as f:
            output_links = requests.get(link)
            f.write(output_links.content)
    except:
        pass