
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ShelterSerializer, PetSerializer
from .models import Shelter, Pet
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView


# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def shelter(request):

    if request.method == 'GET':
        shelter = Shelter.objects.all()
        serializer = ShelterSerializer(shelter, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShelterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def pet(request):

    if request.method == 'GET':
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenPairWithDetailsView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)