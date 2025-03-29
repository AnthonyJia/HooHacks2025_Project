from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import FoodPost

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class FoodPostForm(forms.ModelForm):
    class Meta:
        model = FoodPost
        fields = ["foodname", "description", "image", "pickup_location", "latitude", "longitude", "expiration_time"]

        widgets = {
            "expiration_time": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

