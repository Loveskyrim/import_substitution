from django.contrib.auth import views
from django.urls import path
from .views import products_request, organisations_request

urlpatterns = [
    path(r'products', products_request, name='products'),
    path(r'organisations', organisations_request, name='organisations'),
]