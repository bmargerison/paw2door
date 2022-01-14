from django.urls import path
from . import views

urlpatterns = [
    path('shelter/', views.shelter, name= 'shelters_list'),
    path('pet/', views.pet, name= 'pets_list'),
]