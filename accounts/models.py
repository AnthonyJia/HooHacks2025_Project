from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from geopy.geocoders import Nominatim

class CustomUser(AbstractUser):
    pass

class FoodPost(models.Model):
    foodname = models.CharField(max_length = 255) # Food name
    description = models.TextField() # Food description
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)  # Photo
    pickup_location = models.CharField(max_length=255)  # User inputs this
    latitude = models.FloatField(blank=True, null=True)  # Auto-generated
    longitude = models.FloatField(blank=True, null=True)  # Auto-generated
    expiration_time = models.DateTimeField()  # Post expiration, changable to countdown timer
    created_at = models.DateTimeField(auto_now_add=True)  # Post creation time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Restaurant owner

    def save(self, *args, **kwargs):
        if self.pickup_location and (self.latitude is None or self.longitude is None):
            self.get_lat_lon()
        super().save(*args, **kwargs)

    def get_lat_lon(self):
        geolocator = Nominatim(user_agent="food_app")
        location = geolocator.geocode(self.pickup_location)
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude

    def is_expired(self):
        return timezone.now() > self.expiration_time
    
    def __str__(self):
        return f"{self.foodname} - {self.description[:20]}"
    


