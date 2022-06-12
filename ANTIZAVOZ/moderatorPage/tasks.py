from ANTIZAVOZ.celery import celery_app
import requests
from bs4 import BeautifulSoup as bs
from organisations.models import organisation

import pandas as pd
PATH_TO_FILE_INFO_FIRM = "moderatorPage/static/moderatorPage/Реестр_пром_предприятий_ИНН_название_са.xlsx"


@celery_app.task(name='parse_rbk')
def parse_rbk():
    url = 'https://companies.rbc.ru/categories/'
    page = requests.get(url)
    soup1 = bs(page.text, "html.parser")

    allCategories = soup1.findAll('a', class_='categories__item')
    for i in range(0, len(allCategories)):
        category = allCategories[i].text
        url_of_companies = allCategories[i].get('href')
        page_of_companies = requests.get(url_of_companies)
        soup2 = bs(page_of_companies.text, "html.parser")
        cat_companies = soup2.findAll('a', class_='company-name-highlight') 

        for i in range(0, len(cat_companies)):
            try:
                company_name = cat_companies[i].get('title') + " " + cat_companies[i].text
                url_company = cat_companies[i].get('href')
                page_company = requests.get(url_company)
                soup3 = bs(page_company.text, "html.parser")
                company = soup3.findAll('span', class_='info-cell__text')
                adress = company[2].text
                odrn = company[3].text
                inn = company[4].text
                kpp = company[5].text

                url_director_company = requests.get(url_company + "#founders")
                soup4 = bs(url_director_company.text, "html.parser")
                director = soup4.find('a', class_='link-underlined').text

                url_okved_company = requests.get(url_company + "#okved")
                soup5 = bs(url_okved_company.text, "html.parser")
                okved = soup5.find('span', class_='company-okved__code').text
                
                # print(company_name, okved, category, director, inn, adress)
                organisation.objects.create(
                    organisation_name=company_name,
                    organisation_okved=okved,
                    organisation_category=category,
                    organisation_principal=director,
                    organisation_inn=inn,
                    organisation_adress=adress)
                organisation.save
            except:
                continue



@celery_app.task(name='parse_from_file')
def parse_from_file():
    dfs = pd.read_excel(PATH_TO_FILE_INFO_FIRM, engine="openpyxl")
    print(len(dfs.values))
    organisationsAll = []
    for i in dfs.values:
        id = i[0]
        INN = i[1]
        name = i[2]
        full_name = i[3]
        site = i[4]

        new_company = organisation(
            organisation_name=name,
            organisation_inn=INN,
            organisation_link=site)
        organisationsAll.append(new_company)
    organisation.objects.bulk_create(objs=organisationsAll)

@celery_app.task(name='parse_product_db')
def parse_product_db():
    parse_site("1format.msk.ru")
    # organisationsDB = organisation.objects.all()
    # for orgUnit in organisationsDB:
    #     if (orgUnit.organisation_link):
    #         url = orgUnit.organisation_link
    #         parse_site(url)

CATALOGS_DICT = ['catalog', 'product', 'products', 'goods']
def parse_site(url):
    search_url = url
    if (url[:4] != "http" or url[:5] != "https"):
        search_url = "http://" + url
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                print ('OK!')
            else:
                print ('Boo!')
        except:
            search_url = "https://" + url
    
    page = requests.get(search_url)
    if page.status_code == 200:
        print ('OK!')
    else:
        print("Страница не найдена: ", search_url) 
        return
    
    soup1 = bs(page.text, "html.parser") # поиск по главной странице

    allCategories = soup1.findAll('a')
    words_indexes = {}
    for i in range(0, len(allCategories)):
        word = allCategories[i].text
        word_dict = word.split(" ")
        for w in word_dict:
            w = w.replace("\n", "")
            w = w.replace("\t", "")
            w = w.replace("\r", "")
            if (w in words_indexes):
                words_indexes[w] = words_indexes.get(w) + 1
            else:
                words_indexes[w] = 1
    print(words_indexes)
               




