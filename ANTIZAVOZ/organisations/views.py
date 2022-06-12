from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
def update_product(request):
    if request.method == 'POST':
        name = request.POST['product']
        new_product_name = request.POST['newproductname']
        new_product_description = request.POST['newproductdescription']
        username = str(request.user)

        if ("/" in new_product_name):
            return JsonResponse({}, status=405)
            
        try:
            if (new_product_name != name): # если название отличное от текущего
                existing_product = product.objects.get(
                        product_name=new_product_name)
                if (existing_product): # если такой продукт уже есть
                    return JsonResponse({}, status=402)
        except BaseException:
            pass

        try:
            product_to_update = product.objects.get(product_name=name)
            product_to_update.product_name = new_product_name
            product_to_update.product_description = new_product_description
            product_to_update.save() 
            return JsonResponse({}, status=200)
        except BaseException:
            print('error')
            return JsonResponse({}, status=400)
    return JsonResponse({}, status=400)


@login_required(login_url='/login')
def organisations_request(request):
    employee_list = organisation.objects.all
    return render(request, 'organisations/organisationsList.html', {"employees": employee_list})
