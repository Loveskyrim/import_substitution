from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('index', views.product_list, name='index'),
    path('product/<str:publish>/<str:prod>', views.product_detail, name='product_detail'),
    # path('', views.mainPage, name='index'),
    # path('index', views.mainPage, name='index'),
    # path('getLastProducts', views.getLastProducts, name='getLastProducts'),
]
