from django.db import models
from django.conf import settings
# Create your models here.
class Record(models.Model):
    
    name= models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    number= models.CharField(max_length=255)