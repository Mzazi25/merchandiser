from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from location_field.models.plain import PlainLocationField
from rest_framework.authtoken.models import Token


User = get_user_model()
phone_number_validator = RegexValidator(
    regex=r'^[0-9 \(\)]{10,12}$', message="Phone numbers must begin with +2547.... or 07..."
)
# Create your models here.



class Merchandiser(models.Model):
    username = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15, validators=[phone_number_validator])
    email = models.EmailField()
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.username

    def save_merch(self):
        self.save()

class Manager(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    phone_number = models.CharField(max_length=15, validators=[phone_number_validator])
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.name

    def save_manager(self):
        self.save()

class Address(models.Model):
    city = models.CharField(max_length=255,)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.city

    def save_address(self):
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Address,on_delete=models.CASCADE,related_name="comments", default="")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return str(self.user.user)

    def save_comment(self):
        self.save()

