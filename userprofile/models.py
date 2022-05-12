from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Userinfo(models.Model):
    userinfo_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()
    image = models.CharField(max_length=500, default="https://d25tv1xepz39hi.cloudfront.net/2016-07-16/files/cat-sample_1313.jpg%22")

    """def str(self):
        return self.userinfo_id"""