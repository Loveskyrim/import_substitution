from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .tasks import parse_rbk, parse_from_file
from django.http import JsonResponse


@login_required(login_url='/login')
def moderate_page_request(request):
    return render(request, 'moderatorPage/moderatorPage.html', context={})


# @login_required(login_url='/login')
def update_db(request):
    print('HELLO')
    parse_from_file.delay()
    parse_rbk.delay()
    return JsonResponse({'TEST': 'all right'}, status=200)
