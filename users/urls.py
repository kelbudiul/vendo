# users/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile, signup

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    # Add other authentication-related views and URLs
]
