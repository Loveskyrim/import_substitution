from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def profile_page_request(request):
    return render(request, 'representativePage/representativePage.html', context={})
