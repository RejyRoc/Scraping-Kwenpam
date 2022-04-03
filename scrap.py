import requests as req
from bs4 import BeautifulSoup as bt
import pandas as pd

req = req.get("https://kwenpam.com")
bt = bt(req.text,'html.parser')

if req.status_code ==200: 
    print("Ok")
    data = []
    all_text_item = bt.find_all('div',{'class','text-item'})
    for x_item in all_text_item:
        prix = x_item.find('span', {'class','prix-item'}).get_text()
        livrezon = x_item.find('span', {'class','livraison-item'}).get_text()
        nom_produit = x_item.find('span', {'class','nom-item'}).get_text()

        prix = prix.strip().replace('\r','').replace('\n','')
        livrezon =livrezon.strip().replace('\r','').replace('\n','')
        nom_produit = nom_produit.strip().replace('\r','').replace('\n','')

        data.append({
            'nom':nom_produit,
            'prix':prix,
            'livraison':livrezon
        })
data_frame = pd.DataFrame(data)
data_frame.to_csv('kepam.csv')
        
