from django.shortcuts import render, get_object_or_404
from organisations.models import *


def product_list(request):
    products = product.objects.filter(status__in=('registered', 'Registered'))
    return render(request, 'mainPage/mainPage.html', {'products': products})


def product_detail(request, year, month, day, prod):
    product_item = get_object_or_404(product, slug=prod,
                                     status='published',
                                     publish__year=year,
                                     publish__month=month,
                                     publish__day=day)
    return render(request, 'organisations/product.html', {'product_item': product_item})
