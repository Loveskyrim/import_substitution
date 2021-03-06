from django.contrib.auth import views
from django.urls import path
from .views import products_request, organisations_request, product_request, employee_json, organisation_request

urlpatterns = [
    path(r'organisations', organisations_request, name='organisations'),
    path(r'organisations/<str:inn>', organisation_request, name='organisation_request'),
    path('tag/<str:tag_slug>', products_request, name='post_list_by_tag'),

    path(r'products', products_request, name='products'),   
    path(r'products/<str:publish>/<str:prod>', product_request, name='product'),
    path(r'json/', employee_json, name='json/'),
]