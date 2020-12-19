from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class VaccineCenter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    description = models.TextField(max_length = 255)
    pfp = models.ImageField(upload_to = 'images/')
