from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)
    address = models.CharField(max_length=30)