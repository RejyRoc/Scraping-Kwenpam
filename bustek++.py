import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

host = "https://bustekmedia.com/technologie/"
res = requests.get(f'{host}/fr/blog/')

soup = bs(res.text, 'html.parser')

content_list = soup.find_all('div', {'class': 'td_module_1'})
# print(content_list )
article_list = []

for div in content_list:
    titre = div.find('h3', {'class': 'entry-title'}).text
    link = div.find('h3', {'class': 'entry-title'}).find('a')['href']
    date = div.find('time', {'class': 'entry-date'}).text
    #vue = div.find('div', {'class': 'f-12 mb-0'}).find('span', {'style': 'font-size: 13px;color:#6272af'}).text
    author = div.find('span', {'class','td-post-author-name'}).get_text()
    #tag = div.find('span', {'style': 'font-size: 13px;color:  #777'}).text.replace(",", "-")
   
 
    

    article_list.append({
        "Titre": titre,
        "Lien": link,
        "Date": date,
        "Auteur": author,
        #"Vue": vue,
        #"Tag": tag
    })

print(article_list)
#data = pd.DataFrame(article_list)
#data
