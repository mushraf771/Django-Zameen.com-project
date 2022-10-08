from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_agent= models.BooleanField(default=False)
    is_client= models.BooleanField(default=False)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/clients", blank=True)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.user.username
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.username