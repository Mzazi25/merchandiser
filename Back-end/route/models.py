from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
User = get_user_model()
phone_number_validator = RegexValidator(
    regex=r'^[0-9 \(\)]{10,12}$', message="Phone numbers must begin with +2547.... or 07..."
)
# Create your models here.
class Merchandiser(models.Model):
    username = models.CharField(max_length=40)
    route = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.username.username)

class Manager(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    route_plan =models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    

class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True)
    route = models.CharField(choices=ROUTE_PLAN, default='Unassigned',max_length=20)
    
    def __str__(self):
        return str(self.location)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Route,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    
    def __str__(self):
        return str(self.user.user)

