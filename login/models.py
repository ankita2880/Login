from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False,default="")
    password = models.CharField(max_length=255, null=False, unique=True)
    ifLogged = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=30,null=False,default="")
    token = models.CharField(max_length=255, null=True, default="")
    
    def login_data_dict(self):
    
        return {
            "username":self.username,
            "email":self.email,
            "password":self.password,
            "ifLogged":self.ifLogged,
            "mobile_no":self.mobile_no,
            "token":self.token,
        }


    def __str__(self):
        return "{} -{}".format(self.username, self.email)