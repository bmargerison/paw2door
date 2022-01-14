from django.contrib import admin
from .models import Pet, CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

# Register your models here.
admin.site.register(Pet)
admin.site.register(CustomUser, CustomUserAdmin)