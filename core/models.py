from operator import mod
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.gis.db import models

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, phone_number, location, address, city, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number, location=location, address=address, city=city)

        user.set_password(password)
        user.save()

        return user

# Create your models here.
class Shelter(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    location = models.PointField(null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'location', 'address', 'city']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_full_address(self):
        return self.address + ' ' + self.city

    def __str__(self):
        return self.email

class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name