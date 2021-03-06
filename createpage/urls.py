from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls import url
from django.urls import path


app_name = 'pages'

urlpatterns = [
  path('Resumes', views.createpage, name='createpage'),

]
