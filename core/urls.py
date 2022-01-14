from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithDetailsView, CustomUserCreate, HelloWorldView

urlpatterns = [
    path('shelter/', views.shelter, name= 'shelters_list'),
    path('pet/', views.pet, name= 'pets_list'),
    path('token/obtain/', ObtainTokenPairWithDetailsView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]