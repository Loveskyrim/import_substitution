from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Отображает главную страницу сайта
@login_required(login_url='/login')
def products_request(request):
    return render(request, 'products/productsList.html', context={})
