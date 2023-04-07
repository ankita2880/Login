from django.db import models

# Create your models here.
class login(models.Model):
    username = models.EmailField(max_length=100) 
    password = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    