from django.urls import path
from . import views
from .api import api

urlpatterns = [
    path('home/', views.home, name='home'),
    path('api/', api.urls),
]