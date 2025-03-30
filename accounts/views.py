from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .forms import FoodPostForm
from .models import FoodPost
from django.utils import timezone

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def create_post(request):
    if request.method == 'POST':
        form = FoodPostForm(request.POST, request.FILES)
        if form.is_valid():
            food_post = form.save(commit=False)
            food_post.owner = request.user  # Set the owner field to the current user
            food_post.save()
            return redirect('feed')  # Redirect to homepage after saving
    else:
        form = FoodPostForm()
    return render(request, 'accounts/create_post.html', {'form': form})

def feed_view(request):
    # Get all posts that haven't expired
    available_posts = FoodPost.objects.filter(expiration_time__gt=timezone.now())

    return render(request, 'accounts/feed.html', {'posts': available_posts})

def landing_page(request):
    return render(request,'home.html')