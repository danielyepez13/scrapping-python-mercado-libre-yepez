import requests
from bs4 import BeautifulSoup
import pandas as pd

dates=[]
banks=[]
buys=[]
sells=[]
url= "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
response= requests.get(url)

content = response.text
soup = BeautifulSoup(content, features="html.parser")
for div in soup.find_all('tr', attrs={'class':'letra-pequeña'}):
    date= div.find('span')
    bank= div.find('td', attrs= {'views-field-views-conditional'})
    buy= div.find('td', attrs= {'views-field-field-tasa-compra'})
    sell= div.find('td', attrs={'views-field-field-tasa-venta'})
    dates.append(date.text.strip())
    banks.append(bank.text.strip())
    buys.append(buy.text.strip())
    sells.append(sell.text.strip())

df = pd.DataFrame({'Date':dates, 'Bank':banks, 'Buy':buys, 'Sell':sells}) 
df.to_json('./templates/table.json', orient= 'index')