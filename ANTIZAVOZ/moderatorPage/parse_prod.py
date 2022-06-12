import requests
from bs4 import BeautifulSoup as bs



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

parse_site("1format.msk.ru")