from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import organisation, product


@login_required(login_url='/login')
def products_request(request):
    products_list = product.objects.all
    return render(request, 'organisations/productsList.html', {"products": products_list})

@login_required(login_url='/login')
def product_request(request, product_from_url):
    """функция, отображающая страницу конкретного проекта"""
    try:
        # проверить если ли такой проект в таблице проектов
        current_product = product.objects.get(product_name=product_from_url)
    except Exception as e:
        print(e)
        return render(request, 'product/404.html')

    return render(request, 'organisations/product.html', context={'product_item': current_product})


@login_required(login_url='/login')
def organisations_request(request):
    organisations_list = organisation.objects.all()
    return render(request, 'organisations/organisationsList.html', {"organisations": organisations_list})
