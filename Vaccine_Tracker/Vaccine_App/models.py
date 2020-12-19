from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class VaccineCenter(AbstractBaseUser):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    latitude = models.CharField(max_length = 255)
    longitude = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length=255)
    description = models.TextField(max_length = 255)
    pfp = models.ImageField(upload_to = 'images/')
    distance = models.IntegerField()

    USERNAME_FIELD = 'name'
