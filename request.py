import requests
from bs4 import BeautifulSoup
link = 'https://habr.com/ru/all/'
req = requests.get(link).content
soup2 = BeautifulSoup(req, 'html.parser')
for title in soup2.find_all('h2', {'class': "tm-article-snippet__title"}):
    print(title.a['href'])
    l_link = (title.a['href'])[1:]
    newlink = 'https://habr.com/' + l_link
    req2 = requests.get(newlink).content
    soup_2 = BeautifulSoup(req2, 'html.parser')
    # print(soup_2)
    # for title in soup_2.find_all():
    #     # print(newlink)
    #     # print(title)
    #     # print(soup_2)
    # break