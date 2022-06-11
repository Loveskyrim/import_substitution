from django.contrib.auth import views
from django.urls import path
from .views import moderate_page_request, update_db

urlpatterns = [
    path('moderate', moderate_page_request, name='moderate'),
    path('moderate/update_database', update_db, name='update_db'),
]

