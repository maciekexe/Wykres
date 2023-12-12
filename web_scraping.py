import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


pobranie = requests.get('https://www.worldometers.info/coronavirus/#countries')
soup = BeautifulSoup(pobranie.text, "html.parser")

table = soup.find('table', id='main_table_countries_today')
tbody = table.find('tbody')

liczba_testow = []
kraje = []
Europa = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain',  'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']

for row in tbody.find_all('tr'):
    column = row.find_all('td')
    numer = column[12].text.strip().replace(',', '')
    if numer.isdigit():
        liczba = int(numer)
    kraj = column[1].text.strip()
    if kraj in Europa:
            liczba_testow.append(liczba)
            kraje.append(kraj)
    


plt.tight_layout()  
plt.barh(kraje, liczba_testow)
plt.title("lista zrobionych testów na COVID 19 w krajach europejskich")
plt.ylabel("kraje") 
plt.xlabel("liczba_testów")
plt.show()