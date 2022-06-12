from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .tasks import parse_rbk, parse_from_file, parse_product_db, parse_okved_db, parse_fabricator_db
from django.http import JsonResponse


@login_required(login_url='/login')
def moderate_page_request(request):
    return render(request, 'moderatorPage/moderatorPage.html', context={})


# @login_required(login_url='/login')
def update_db(request):
    parse_from_file.delay()
    # parse_rbk.delay()
    return JsonResponse({'TEST': 'all right'}, status=200)

def parse_product_by_db(request):
    parse_product_db.delay()
    return JsonResponse({'TEST': 'all right'}, status=200)

def parse_okved(request):
    parse_okved_db.delay()
    return JsonResponse({'TEST': 'all right'}, status=200)

def parse_fabricator(request):
    parse_fabricator_db.delay()
    return JsonResponse({'TEST': 'all right'}, status=200)
