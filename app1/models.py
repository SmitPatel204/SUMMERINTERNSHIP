from django.db import models

# Create your models here.

class Appmodel(models.Model):
    FirstName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.PositiveBigIntegerField()
    Address = models.TextField()
    Email = models.EmailField()
    Password = models.CharField(max_length=15)