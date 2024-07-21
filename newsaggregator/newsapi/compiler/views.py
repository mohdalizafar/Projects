

# Create your views here.
from django.shortcuts import render
from .models import News
from rest_framework import generics
from .serializer import NewsSerializer


class NewsView( generics.ListAPIView):
    
    serializer_class= NewsSerializer
    queryset=News.objects.all()
