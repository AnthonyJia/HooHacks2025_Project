from django.contrib import admin
from .models import CustomUser, FoodPost

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(FoodPost)