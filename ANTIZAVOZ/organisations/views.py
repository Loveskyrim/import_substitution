from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import organisation


@login_required(login_url='/login')
def products_request(request):
    return render(request, 'organisations/productsList.html', context={})


@login_required(login_url='/login')
def organisations_request(request):
    organisations_list = organisation.objects.all()
    return render(request, 'organisations/organisationsList.html', {"organisations": organisations_list})
