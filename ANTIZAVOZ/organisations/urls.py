from django.contrib.auth import views
from django.urls import path
from .views import products_request, organisations_request, product_request
from mainPage.views import product_detail

urlpatterns = [
    path(r'products', products_request, name='products'),
    # path(r'products/<str:product_from_url>', product_request, name='product'),
    path(r'organisations', organisations_request, name='organisations'),
    path('products/<str:publish>/<str:prod>', product_request, name='product'),
]
