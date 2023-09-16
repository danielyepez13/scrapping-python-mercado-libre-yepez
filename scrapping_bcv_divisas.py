# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"

# names=[]
# prices=[]
# response = requests.get(url)

#pip install selenium
#pip install pandas
#pip3 install beautifulsoup4

# content = response.text
# soup = BeautifulSoup(content, features="html.parser")
# for div in soup.findAll('div', attrs={'class':'row recuadrotsmc'}):
#     name=div.find('span')
#     price=div.find('strong')
#     names.append(name.text)
#     prices.append(price.text)

# resultsName = []
# i = 0
# for element in names:
#     resultsName.append(element + ": "+prices[i])
#     i+=1


# df = pd.DataFrame({'Name money':resultsName}) 
# df.to_json('prices_bcv.json')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

names=[]
prices=[]
url= "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
response= requests.get(url)

content = response.text
soup = BeautifulSoup(content, features="html.parser")
for div in soup.findAll('div', attrs={'row recuadrotsmc'}):
    name=div.find('span')
    price=div.find('strong')
    names.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Coin Name':names,'Price':prices}) 
df.to_csv('prices.csv', index=False, encoding='utf-8')

csvFilePath= 'prices.csv'
jsonFilePath= 'prices.json'

jsonArray = []

#read csv file
with open(csvFilePath, encoding='utf-8') as csvf: 
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf) 

    #convert each csv row into python dict
    for row in csvReader: 
        #add this python dict to json array
        jsonArray.append(row)

#convert python jsonArray to JSON String and write to file
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(jsonArray, indent=4)
    jsonf.write(jsonString)