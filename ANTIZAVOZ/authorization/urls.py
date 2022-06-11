from django.contrib.auth import views
from django.urls import path
from .views import register_request, login_request, logout_request

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path("register/", register_request, name="register"),
]