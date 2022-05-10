from django.db import models


# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()
    image = models.CharField(max_length=500, default="https://d25tv1xepz39hi.cloudfront.net/2016-07-16/files/cat-sample_1313.jpg")

    def __str__(self):
        return self.name


