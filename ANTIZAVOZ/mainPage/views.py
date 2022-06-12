from django.shortcuts import render, redirect, get_object_or_404
from organisations.models import *
import datetime
from django.contrib.auth.models import User


def product_list(request):
    organisations = organisation.objects.filter(author=User.objects.get(username=request.user))
    products = product.objects.filter(author__in=organisations, status__in=('registered', 'Registered'))
    # products = product.objects.all()
    return render(request, 'mainPage/mainPage.html', context={'organisations': organisations, 'products': products})


def product_detail(request, publish, prod):
    product_item = get_object_or_404(product, slug=prod,
                                     status='registered',
                                     publish__year=publish.split('.')[2],
                                     publish__month=publish.split('.')[1],
                                     publish__day=publish.split('.')[0])
    return render(request, 'organisations/product.html', context={'product_item': product_item})


def organisation_detail(request, publish, prod):
    organisation_item = get_object_or_404(organisation, slug=prod,
                                          status='registered',
                                          publish__year=publish.split('.')[2],
                                          publish__month=publish.split('.')[1],
                                          publish__day=publish.split('.')[0])
    return render(request, 'organisations/organisation.html', context={'organisation_item': organisation_item})


def organisation_create(request):

    org = organisation.objects.create(
                organisation_name=request.company_name,
                organisation_okved=request.okved,
                organisation_category=request.category,
                organisation_principal=request.director,
                organisation_inn=request.inn,
                organisation_adress=request.adress)
    return redirect('index')
