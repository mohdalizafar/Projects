

# Create your models here.
from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=250)
    url=models.TextField(primary_key=True)
    source=models.CharField(max_length=100)
    author=models.CharField(max_length=150)

    class Meta:
        db_table="NEWSITES"
        managed=False
