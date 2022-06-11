from django.shortcuts import render, get_object_or_404
from organisations.models import *
import datetime


def product_list(request):
    products = product.objects.filter(status__in=('registered', 'Registered'))
    # products = product.objects.all()
    return render(request, 'mainPage/mainPage.html', context={'products': products})


def product_detail(request, publish, prod):
    print(publish)
    product_item = get_object_or_404(product, slug=prod,
                                     status='registered',
                                     publish__year=publish.split('.')[2],
                                     publish__month=publish.split('.')[1],
                                     publish__day=publish.split('.')[0])
    return render(request, 'organisations/product.html', context={'product_item': product_item})
