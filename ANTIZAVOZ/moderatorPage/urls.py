from django.contrib.auth import views
from django.urls import path
from .views import moderate_page_request, parse_from_file

urlpatterns = [
    path('moderate', moderate_page_request, name='moderate'),
    path('moderate/update_database', parse_from_file, name='update_db'),
]

