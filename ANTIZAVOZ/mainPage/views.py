from django.shortcuts import render, redirect, get_object_or_404
from organisations.models import *
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import createOrganisationFormModal
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.utils.formats import date_format
from unidecode import unidecode

@login_required(login_url='/login')
def product_list(request):
    products_list = product.objects.all()
    canva_categories = {}
    for prod in products_list:
        if (prod.product_tags in canva_categories):
            canva_categories[prod.product_tags] += 1
        else:
            canva_categories[prod.product_tags] = 1
    
    sorted_x = sorted(canva_categories.items(), key=lambda kv: kv[1])

    # result = {key: a[key] for key in a.keys() if key in targets}
    # print(json.dumps(result, indent = 15))


    ready_modalForm = createOrganisationFormModal(request.POST)
    if ready_modalForm.is_valid():
        try:
            if '/' in ready_modalForm.cleaned_data['organisation_name']:
                messages.error(
                    request,
                    "Ошибка! Символ слеша в имени: " + ready_modalForm.cleaned_data['organisation_name'])
                return redirect('/index')

            if len(ready_modalForm.cleaned_data['organisation_name']) > 200:
                messages.error(
                    request,
                    "Ошибка! Длина имени не должна превышать 200 символов!")
                return redirect('/index')
            print(slugify(unidecode(ready_modalForm.cleaned_data['organisation_name'])))
            new_organisation = organisation.objects.create(
                organisation_name=ready_modalForm.cleaned_data['organisation_name'],
                organisation_adress=ready_modalForm.cleaned_data['organisation_adress'],
                author=User.objects.get(username=request.user),
                organisation_inn=ready_modalForm.cleaned_data['organisation_inn'],
                organisation_okved=ready_modalForm.cleaned_data['organisation_okved'],
                slug=slugify(unidecode(ready_modalForm.cleaned_data['organisation_name'])),
                status='draft')
            messages.success(
                request, "Организация " + ready_modalForm.cleaned_data['organisation_name'] + " успешно создана!")
        except Exception as e:
            print(e)
            messages.error(
                request, "Организация " + ready_modalForm.cleaned_data['organisation_name'] + " уже существует!")
            return redirect('/index', context={"canvaCategories": canva_categories.keys, "canvaValues": canva_categories.values})
        if 'continue' in request.POST:

            return redirect(f"organisation/{str(date_format(new_organisation.publish, format='SHORT_DATE_FORMAT', use_l10n=True))}/{slugify(unidecode(ready_modalForm.cleaned_data['organisation_name']))}")

    createOrganisationModalForm = createOrganisationFormModal()

    organisations = organisation.objects.filter(author=User.objects.get(username=request.user))
    products = product.objects.filter(author__in=organisations, status__in=('registered', 'Registered'))

    return render(request, 'mainPage/mainPage.html', context={'form': createOrganisationModalForm, 'organisations': organisations[:10], 'products': products, "canvaCategories": canva_categories.keys, "canvaValues": canva_categories.values})


@login_required(login_url='/login')
def product_detail(request, publish, prod):

    product_item = get_object_or_404(product, slug=prod,
                                     publish__year=publish.split('.')[2],
                                     publish__month=publish.split('.')[1],
                                     publish__day=publish.split('.')[0])
    return render(request, 'organisations/product.html', context={'product_item': product_item})


@login_required(login_url='/login')
def organisation_detail(request, publish, prod):
    organisation_item = get_object_or_404(organisation, slug=prod,
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
