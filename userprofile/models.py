from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Userinfo(models.Model):
    userinfo_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=500, null=True)

    """def str(self):
        return self.userinfo_id"""