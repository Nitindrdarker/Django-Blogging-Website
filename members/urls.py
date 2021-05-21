from django.contrib import admin
from django.contrib import auth
from .views import CreateProfilePage, EditProfilePageView, ShowProfileView, UserEditView, UserRegistrationView, password_success, PasswordsChangeView
from django.urls import path
from django.contrib.auth import views as auth_views #views com with django

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),#by default the address is '/password' in of change password form
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page')
]