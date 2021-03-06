from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('logout', views.logout_views, name='logout'),
    path('login', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete"),

]
