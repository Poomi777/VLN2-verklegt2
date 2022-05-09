from django.db import models


# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


