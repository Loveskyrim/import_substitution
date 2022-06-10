from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'index', views.product_list, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<prod>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    # path('', views.mainPage, name='index'),
    # path('index', views.mainPage, name='index'),
    # path('getLastProducts', views.getLastProducts, name='getLastProducts'),
]
