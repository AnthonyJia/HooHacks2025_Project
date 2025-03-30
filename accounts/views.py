from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .forms import FoodPostForm
from .models import FoodPost
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

@login_required
def edit_post_view(request, post_id):
    post = get_object_or_404(FoodPost, id=post_id)

    if post.owner != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = FoodPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change to the actual URL name
    else:
        form = FoodPostForm(instance=post)

    return render(request, 'accounts/edit_post.html', {'form': form, 'post': post})