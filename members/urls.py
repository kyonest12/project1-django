from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('register/', userRegisterForm.as_view(), name = 'register_page'),
    path('edit_account_profile/', userEditForm.as_view(), name = 'edit_account_profile'),
    path('password/', passwordChangeView.as_view()),
    path('password_change_success', passwordChangeSuccess, name = 'password_change_success'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.
         as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.
         as_view(template_name="registration/form_password_reset.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name="registration/password_reset_success.html"),
         name="password_reset_complete"),
]
