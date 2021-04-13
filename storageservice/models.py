from django.db import models

# Create your models here.
class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    unit = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField()
