from django.urls import path
from .views import signup_view, login_view, logout_view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('feed/', views.feed_view, name='feed'),
    path('create/', views.create_post, name='create_post'),
    path('',views.landing_page, name = 'home'),
    path('post/<int:post_id>/edit/', views.edit_post_view, name='edit_post'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)