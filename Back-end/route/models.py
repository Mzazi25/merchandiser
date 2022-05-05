from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import CharField, EmailField
from importlib_metadata import email
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_merchandiser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @receiver(post_save,sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender,instace=None,created=False,**kwargs):
        if created:
            Token.objects.create(user=instace)

class Merchandiser(models.Model):
    name= models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='merchandiser')
    area = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name.username

class Manager(models.Model):
    manager = models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='manager')
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.manager.username