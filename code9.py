import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

host = "https://code9haiti.com"
res = requests.get(f'{host}/fr/blog/')

soup = bs(res.text, 'html.parser')

content_list = soup.find_all('article', {'class': 'blog-preview'})
# print(content_list )
article_list = []

for div in content_list:
    titre = div.find('h5', {'class': 'mt-1 bold'}).text
    link = div.find('h5', {'class': 'mt-1 bold'}).find('a')['href']
    date = div.find('span', {'class': 'gray'}).text
    vue = div.find('div', {'class': 'f-12 mb-0'}).find('span', {'style': 'font-size: 13px;color:#6272af'}).text
    author = div.find('a').text
    tag = div.find('span', {'style': 'font-size: 13px;color:  #777'}).text.replace(",", "-")

    article_list.append({
        "Titre": titre,
        "Lien": host + link,
        "Date": date,
        "Auteur": author,
        "Vue": vue,
        "Tag": tag
    })

print("Create Dataframe ...")
data = pd.DataFrame(article_list)
data.to_csv('codeblog.csv')
print("Saving Dataframe to CSV")

print("\nEND SCRIPT")
