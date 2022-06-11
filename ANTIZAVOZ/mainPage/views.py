from django.shortcuts import render, get_object_or_404
from organisations.models import *


def product_list(request):
    products = product.objects.filter(status__in=('registered', 'Registered'))
    # products = product.objects.all()
    return render(request, 'mainPage/mainPage.html', context={'products': products})


def product_detail(request, publish, prod):
    print(publish)
    product_item = get_object_or_404(product, slug=prod,
                                     status='registered',
                                     publish=publish.strptime(publish, "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"))
    return render(request, 'organisations/product.html', context={'product_item': product_item})
