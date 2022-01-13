"""paw2door URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, views
from core import views
from core.views import front
from django.shortcuts import render

router = routers.DefaultRouter()
router.register(r'shelter', views.ShelterView, 'shelter')
router.register(r'pet', views.PetView, 'pet')

# def index_view(request):
#     return render(request, 'build/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('core.urls')),
    path("", front, name="front"),
    # path('', index_view, name='index'),
]

#path('api/', include('core.urls')),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)