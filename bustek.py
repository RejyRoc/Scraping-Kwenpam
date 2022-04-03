import requests as req
from bs4 import BeautifulSoup as bt
import pandas as pd

req = req.get("https://bustekmedia.com/technologie/")
bt = bt(req.text,'html.parser')

if req.status_code ==200: 
    print("Ok")
    data = []
    all_text_item = bt.find_all('div',{'class','td_module_1'})
    for x_item in all_text_item:
        date  = x_item.find('time', {'class','entry-date'}).get_text()
        titre  = x_item.find('h3', {'class','entry-title'}).get_text()
       

        #date= date.strip().replace('\r','').replace('\n','')
        #titre =titre.strip().replace('\r','').replace('\n','')
       

        data.append({
            'date':date,
            'titre':titre,
            
        })
    print(data)
data_frame = pd.DataFrame(data)
data_frame.to_csv('ayibo.csv')
        
