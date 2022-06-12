from django.contrib.auth import views
from django.urls import path
from moderatorPage.views import moderate_page_request, update_db, parse_product_by_db

urlpatterns = [
    path('moderate', moderate_page_request, name='moderate'),
    path('moderate/update_database', update_db, name='update_db'),
    path('moderate/update_productsdb', parse_product_by_db, name='parse_product_by_db')
]

