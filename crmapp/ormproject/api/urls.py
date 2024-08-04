from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
   
     path("login/", views.login_user,name="login") ,
     path("",views.register_user,name="register") ,
     path("main/" , views.mainview, name="main") ,
     path('lout/', views.logout_user, name='logout'),
     path("record/<int:pk>/", views.customer_record, name="record") ,
     path( "delete_page/<int:pk>/", views.delete_record, name="delete") ,
     path('addrecord/', views.add_record, name='add'),
     path('modifyrecord/<int:pk>/', views.modify_record, name='modify'),


]