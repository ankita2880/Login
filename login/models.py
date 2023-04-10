from django.db import models

from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False,default="")
    password = models.CharField(max_length=255, null=False, unique=True)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)