from unicodedata import category
from ANTIZAVOZ.celery import celery_app
import requests
from bs4 import BeautifulSoup as bs
from organisations.models import organisation, product, okved

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

@celery_app.task(name='parse_okved_db')
def parse_okved_db():
    page = requests.get("https://xn----dtbec0aczc1l.xn--p1ai/")
    soup1 = bs(page.text, "html.parser") 

    allKodes = soup1.findAll('td')
    for i in range(0, len(allKodes), 2):
        id_okved = allKodes[i].text
        id_okved = id_okved.replace(" ", "")
        desc = allKodes[i+1].text
        name = ""
        description = ""
        if ("\n" in desc):
            desc_arr = desc.split("\n")
            name = desc_arr[0].replace("\t", "")
            description = desc.replace(desc_arr[0]+"\n", "")
        # print(id_okved + "\n" +  name + "\n" + description)
        okved.objects.get_or_create(id_okved=id_okved, name=name, description=description)
        okved.save


ACTUAL_CATEGORIES_FABRICATOR = [['12430','Лесная промышленность'],
['12436','Машиностроение и металообработка'],
['12471','Медицинская промышленность'],
['12474','Металлургия'],
['12482','Мукомольно-крупяная промышленность'],
['12487','Пищевая промышленность'],
['12500','Стройматериалы и товары для ремонта'],
['12508','Прочие промышленные производства'],
['12512','Сельское хозяйство'],
['12516','Стекольная и фарфоро-фаянсовая промышленность'],
['12519','Нефтехимическая промышленность'],
['14200','Горная промышленность'],
['14258','Промышленное оборудование'],
['14259','Транспортное машиностроение'],
['12422','Легкая промышленность']]
URL = 'https://fabricators.ru/zavody?region=11800&product=12474'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0', 'accept': '*/*'}
graf_array = []

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_pages_count(html):
    soup = bs(html, 'html.parser')
    pagination = soup.find_all('li', class_='pager-item')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1
def split_by_coma(desc):
    product_array = []
    if (", " in desc):
        product_array = desc.split(',')
    else:
        product_array = [desc]
    result_array = []
    for prod in product_array:
        result_array.append(prod.replace('.', '').strip()) 
    return result_array

def save_products(desc, sep, comp, cat):
    desc_array = desc.split(sep)
    products = split_by_coma(desc_array[1])
    for prod in products:
        if (len(prod)>5):
            # print(desc + " - " +prod) TODO author!
            product.objects.get_or_create(product_name=prod,
                                    author=comp,
                                    product_tags=cat)
            product.save


def get_content(html, category):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='content-list-item enterprise-teaser')

    promisel = []
    for item in items:
        organisation_name=item.find('a', class_='title-site--h3').get_text(strip=True)
        organisation_category=category
        organisation_adress=item.find('p', class_='text--col1').get_text(strip=True)
        organisation_description = item.find('div', class_='field-item even').get_text(strip=True)

        comp_exists = organisation.objects.filter(organisation_name=organisation_name.replace("',)", "").replace("('", ""),
                organisation_category=organisation_category.replace("',)", "").replace("('", ""),
                organisation_adress=organisation_adress.replace("',)", "").replace("('", ""),
                organisation_description=organisation_description.replace("',)", "").replace("('", "")).exists()
        if not comp_exists:
            new_company = organisation.objects.create(organisation_name=organisation_name.replace("',)", "").replace("('", ""),
                organisation_category=organisation_category.replace("',)", "").replace("('", ""),
                organisation_adress=organisation_adress.replace("',)", "").replace("('", ""),
                organisation_description=organisation_description.replace("',)", "").replace("('", ""))
        else:
            print("Компания", organisation_name, "уже существует")
            return

        promisel.append(1)
        if (": " in organisation_description):
            save_products(organisation_description, ": ", new_company, category)
        elif ("реализует " in organisation_description.lower()):
            save_products(organisation_description.lower(), "реализует ", new_company, category)
        elif ("производим " in organisation_description.lower()):
            save_products(organisation_description.lower(), "производим ", new_company, category)
        elif ("производит " in organisation_description.lower()):
            save_products(organisation_description.lower(), "производит ", new_company, category)
    return promisel

def parse(url, category):
    URL = 'https://fabricators.ru/zavody?region=11800&product=' + url
    html = get_html(URL)
    if html.status_code == 200:
        array = []
        pages_count = get_pages_count(html.text)
        for page in range(0, pages_count):
            html = get_html(URL, params={'page': page})
            array.append(get_content(html.text, category))
        # print(array)
        graf_array.append((len(array), category))
    else:
        print('ERROR')

@celery_app.task(name='parse_fabricator')
def parse_fabricator_db():
    for i in ACTUAL_CATEGORIES_FABRICATOR:
        parse(i[0],i[1])


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
                return
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
               




