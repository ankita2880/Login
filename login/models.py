from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128,null=True,blank = True)
    mobile_no = models.BigIntegerField()

    def __str__(self):
        return self.username