from ast import Add
from email.policy import default
from signal import default_int_handler
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.gis.geos import Point

from django.contrib.auth import get_user_model
from location_field.models.plain import PlainLocationField
from django import forms

User = get_user_model()
phone_number_validator = RegexValidator(
    regex=r'^[0-9 \(\)]{10,12}$', message="Phone numbers must begin with +2547.... or 07..."
)
# Create your models here.
class Merchandiser(models.Model):
    username = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    email = models.EmailField()
    location = PlainLocationField(based_fields=['city'], zoom=7, default = '')
    def __str__(self):
        return str(self.username.username)

class Manager(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    location = PlainLocationField(based_fields=['city'], zoom=7, default ="")

class Address(models.Model):
    city = models.CharField(max_length=255,)
    location = PlainLocationField(based_fields=['city'], zoom=7)


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Address,on_delete=models.CASCADE,related_name="comments", default="")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return str(self.user.user)

