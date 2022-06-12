from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import organisation, product


@login_required(login_url='/login')
def products_request(request):
    products_list = product.objects.all()
    return render(request, 'organisations/productsList.html', {"products": products_list})


@login_required(login_url='/login')
def product_request(request, publish, prod):
    print(prod)
    product_item = get_object_or_404(product, product_name=prod,
                                     publish__year=publish.split('.')[2],
                                     publish__month=publish.split('.')[1],
                                     publish__day=publish.split('.')[0])
    return render(request, 'organisations/product.html', context={'product_item': product_item})


@login_required(login_url='/login')
def organisations_request(request):
    organisations_list = organisation.objects.all()
    return render(request, 'organisations/organisationsList.html', {"organisations": organisations_list})
