from django.contrib.auth import views
from django.urls import path
from .views import profile_page_request

urlpatterns = [
    path('profile', profile_page_request, name='profile'),
]