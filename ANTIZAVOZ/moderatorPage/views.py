from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import requests
from bs4 import BeautifulSoup as bs
# from django.apps import apps
from organisations.models import organisation
from django.http import JsonResponse


@login_required(login_url='/login')
def moderate_page_request(request):
    return render(request, 'moderatorPage/moderatorPage.html', context={})

# @login_required(login_url='/login')
def update_db():
    print('HELLO')
    parse_rbk()


def parse_rbk():
    # organisation = apps.get_model('organisations', 'organisation')
    print('parse!!!!')
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

            organisation.objects.create(
                organisation_name = company_name,
                organisation_okved = okved,
                organisation_category = category,
                organisation_principal = director,
                organisation_inn = inn,
                organisation_adress = adress)
            organisation.save()
            
        print('\n')
    return JsonResponse({'TEST': 'all right'}, status=200)
