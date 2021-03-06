from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls import url
from django.urls import path


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('form/', views.newProfile, name='profile_form'),
    path('updateinfo/', views.update_profile, name='updateinfo'),
    path('CV/<id>/', views.generate, name='generate'),
    path('addCvDetails', views.addcvdetail, name='updateform1'),
    path('addCVDetails2', views.addcvdetail2, name='resumeform2'),
    path('generatecv', views.generateCV, name='generatecv'),
    path('selectcv', views.selectcv, name='selectcv'),
    path('addEmployeepic', views.addpic, name='employeepic'),
    path('printcv/<id>', views.printcv, name='printcv'),
    path('printblackcv/<id>', views.printcvblack, name='printblackcv'),
    path('generateblackcv/<id>', views.generateCV2, name='generateblackcv')

]
