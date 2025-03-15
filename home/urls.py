from . import views
from django.urls import path



urlpatterns = [
    path('',views.app, name='login'),
    path('signup/',views.sign, name='signup'),
    path('homepage/',views.homepage, name='homepage'),
    path('newpost/',views.newpost,name='newpost'),
    path('mypost/',views.mypost, name='mypost'),
    path('signout/',views.signout, name='signout'),


    ]

