from django.urls import path
from .views import signup_view, login_view, logout_view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)