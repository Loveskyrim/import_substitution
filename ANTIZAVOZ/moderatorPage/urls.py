from django.contrib.auth import views
from django.urls import path
from moderatorPage.views import moderate_page_request, update_db, parse_product_by_db, parse_okved, parse_fabricator

urlpatterns = [
    path('moderate', moderate_page_request, name='moderate'),
    path('moderate/update_database', update_db, name='update_db'),
    path('moderate/update_productsdb', parse_product_by_db, name='parse_product_by_db'),
    path('moderate/update_okveddb', parse_okved, name='parse_okved'),
    path('moderate/parse_fabricatordb', parse_fabricator, name='parse_fabricator')

]

