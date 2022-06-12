from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import organisation, product
from taggit.models import Tag
from django.db.models import Count


@login_required(login_url='/login')
def products_request(request, tag_slug=None):
    products_list = product.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products_list = products_list.filter(product_tags__in=[tag])

    return render(request, 'organisations/productsList.html', {"products": products_list,
                                                               "tag": tag})


@login_required(login_url='/login')
def product_request(request, publish, prod):
    print(prod)
    product_item = get_object_or_404(product, product_name=prod,
                                     publish__year=publish.split('.')[2],
                                     publish__month=publish.split('.')[1],
                                     publish__day=publish.split('.')[0])
    product_tags_ids = product_item.product_tags.values_list('id', flat=True)
    similar_products = product.objects.filter(product_tags__in=product_tags_ids).exclude(id_product=product_item.id_product)
    print('Похожее:', similar_products)
    similar_products = similar_products.annotate(same_tags=Count('product_tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'organisations/product.html', context={'product_item': product_item,
                                                                  'similar_products': similar_products})


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


def organisation_request(request, inn):
    org_item = get_object_or_404(organisation, organisation_inn=inn)
    return render(request, 'organisations/organisation.html', context={'organisation_item': org_item})


@login_required(login_url='/login')
def organisations_request(request):
    organisations_list = organisation.objects.all()
    return render(request, 'organisations/organisationsList.html', {"organisations": organisations_list})
    
@login_required(login_url='/login')
def employee_json(request):
    employees = organisation.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)