import requests
from bs4 import BeautifulSoup
import pandas as pd

names=[]
prices=[]
url= "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
response= requests.get(url)

content = response.text
soup = BeautifulSoup(content, features="html.parser")
for div in soup.findAll('div', attrs={'row recuadrotsmc'}):
    name=div.find('span')
    price=div.find('strong')
    names.append(name.text.strip())
    prices.append(price.text.strip())

coins = {}
for idx, x in enumerate(names):
    coins[names[idx]] = prices[idx]

df = pd.DataFrame({"Coins": coins})
df.to_json("templates/prices.json")