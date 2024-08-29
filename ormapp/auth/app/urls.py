from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path( "", views.loginpage, name="login" ) ,
    path("sign/", views.signpage, name="sign") ,
]