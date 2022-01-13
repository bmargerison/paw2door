from django.urls import path
from . import views

urlpatterns = [
    path('shelter/', views.ShelterView.as_view({'get': list}), name= 'shelters_list'),
    path('pet/', views.PetView.as_view({'get': list}), name= 'pets_list'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.session_view, name='api-session'),
    path('whoami/', views.whoami_view, name='api-whoami'),
]