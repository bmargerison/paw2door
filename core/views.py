import json

from django.http import request
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models.query import QuerySet
from rest_framework import status, viewsets
from .serializers import ShelterSerializer, PetSerializer
from .models import Shelter, Pet
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST


# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

class ShelterView(viewsets.ModelViewSet):
    serializer_class = ShelterSerializer
    queryset = Shelter.objects.all()

class PetView(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

@require_POST
def login_view(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return JsonResponse({'detail': 'Please provide email and password.'}, status=400)

    user = authenticate(email=email, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'email': request.user.email})