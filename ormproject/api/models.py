from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField( auto_now_add = True)
    First_Name= models.CharField( max_length = 255)
    Last_Name= models.CharField( max_length=255)
    Email = models.EmailField()
    City = models.CharField( max_length=255)
    Phone= models.CharField( max_length=255)

    def __str__(self):
        return ( f"{self.First_Name} {self.Last_Name}")