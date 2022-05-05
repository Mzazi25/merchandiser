
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class User(AbstractUser):
    is_manager =models.BooleanField(default=False)
    is_merchandiser =models.BooleanField(default=False)
    def __str__(self):
        return self.username

    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Merchandiser(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='merchandiser')
    area = models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='manager')
    company = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.user.username