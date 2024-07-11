from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path("", views.register, name="register") ,
    path("loginpage/", views.loginpage, name="login") ,
    path('admin/', admin.site.urls) ,
    path("home/", views.home, name="home")
]