# from psycopg2 import connect

import psycopg2 as pgdb
import requests
from bs4 import BeautifulSoup as bs
from organisations.models import organisation

CONNECTPARAM = 'host=127.0.0.1 port=5432 dbname=antizavozdb user=django_admin password=1234567'
try:
    connection = pgdb.connect(CONNECTPARAM)
    cursor = connection.cursor()
except:
    print("Unable to connect")
    exit(1)

cursor.execute('SELECT version()')
db_version = cursor.fetchone()


url = 'https://companies.rbc.ru/categories/'
# payload = {"page":1,"per_page":15,"filters":{"status_code":"product","region_ids":[365]}}
# page = requests.get(url, data=json.dumps(payload))
page = requests.get(url)
soup1 = bs(page.text, "html.parser")

allCategories = soup1.findAll('a', class_='categories__item')
for i in range(0, len(allCategories)):
    category = allCategories[i].text
    print(category) 
    url_of_companies = allCategories[i].get('href')
    page_of_companies = requests.get(url_of_companies)
    soup2 = bs(page_of_companies.text, "html.parser")
    cat_companies = soup2.findAll('a', class_='company-name-highlight')

    for i in range(0, len(cat_companies)): 
        company_name =  cat_companies[i].get('title')    
        print( company_name + " " + cat_companies[i].text) 
        url_company = cat_companies[i].get('href')
        page_company = requests.get(url_company)
        soup3 = bs(page_company.text, "html.parser")
        company = soup3.findAll('span', class_='info-cell__text')
        adress = company[2].text
        odrn = company[3].text
        inn = company[4].text
        kpp = company[5].text

        director = soup3.find('a', class_='info-cell__text link-underlined strong').text

        url_okved_company = requests.get(url_company+"#okved")
        soup4 = bs(url_okved_company.text, "html.parser")
        okved = soup3.find('span', class_='company-okved__code').text

        new_organisation = organisation.objects.create(
            organisation_name = company_name,
            organisation_okved = okved,
            organisation_category = category,
            organisation_principal = director,
            organisation_inn = inn,
            organisation_adress = adress)

        # SQL = "INSERT INTO organisations_organisation "
        # SQL += "(organisation_name, organisation_adress, organisation_inn, organisation_category, organisation_principal, organisation_okved, "
        # SQL += " id_organisation, author, slug, publish, created, updated, organisation_description, organisation_link, organisation_sanctions, status) SELECT '"
        # SQL += str(company_name) + "', '" + str(adress) + "', '" + str(inn) + "', '" + str(category) + "', '" + str(director) + "', '" + str(okved) + "'"
        # SQL += " WHERE NOT EXISTS(SELECT organisation_name FROM organisations_organisation WHERE organisation_name = '" + company_name
        # SQL += "')  ON CONFLICT DO NOTHING;"
        # cursor.execute(SQL)
        # connection.commit()

        organisation.objects.bulk_create(objs=new_organisation)
        
    print('\n')
