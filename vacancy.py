import requests
from bs4 import BeautifulSoup
import json



link = 'https://career.habr.com/vacancies?type=all'
# link = 'https://career.habr.com/vacancies?page=2&type=all'
pages = []
vacancies = []
pages.append(link)

def write_json(data, filename= 'vacancies.json'):
    with open('vacancies.json', 'r+') as file:
        json.dump(data, file, indent=4)


for i in range(2, 11):
    pages.append('https://career.habr.com/vacancies?'+'page='+str(i)+'type=all')
req = requests.get(link).content
soup = BeautifulSoup(req, 'html.parser')

for l in pages:
    req = requests.get(l).content
    soup2 = BeautifulSoup(req, 'html.parser')
    for title in soup2.find_all('a', {'class': "vacancy-card__title-link"}):
        vac_link = (str(title)).split()[2]
        vac = vac_link[(vac_link.index('"')):]
        vac = vac.replace('"', ' ')
        vac = vac.split()
        vacancy_link = vac[0]
        # vacancies.append(vacancy_link)
        page_link = 'https://career.habr.com' + vacancy_link
        req = requests.get(page_link).content
        soup = BeautifulSoup(req, 'html.parser')
        dict = {

        }

        for header in soup.find_all('h1', {'class': "page-title__title"}):
            name = header.get_text()
            dict['name'] = str(name)

        for money in soup.find_all('div', {'class': "basic-salary basic-salary--appearance-vacancy-header"}):
            salary = money.get_text()
            dict['salary'] = str(salary)
            # with open('vacancies.json') as file:
            #     data = json.load(file)
            #     temp = data["vacancies"]
            #     y = {"salary": str(salary)}
            #     temp.append(y)
            # write_json(data)

        for quols in soup.find_all('a', {'class': "link-comp link-comp--appearance-dark"}):
            quolification = quols.get_text()
            dict['qualification'] = str(quolification)

        for place in soup.find_all('span', {'class': "preserve-line"}):
            conditionals = place.get_text()
            dict['conditions'] = str(conditionals)
        for desc in soup.find_all('div', {'class': "collapsible-description"}):
            description = desc.get_text()
            dict['description'] = str(description)

        with open('vacancies.json') as file:
            data = json.load(file)
            temp = data["vacancies"]
            y = dict
            temp.append(y)
        write_json(data)