from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
User = get_user_model()
phone_number_validator = RegexValidator(
    regex=r'^[0-9 \(\)]{10,12}$', message="Phone numbers must begin with +2547.... or 07..."
)
# Create your models here.
class Merchandiser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='name')
    route = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.username.username)

class Manager(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='manager')
    description = models.TextField(blank=True)
    route_plan = models.ManyToManyField(User,blank=True,related_name='route_plan')
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    location = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.name.name)
    @property
    def route_plan(self):
        return self.route_plan.all().count()
ROUTE_PLAN = (
    ('Assigned', 'Unassigned'),
    ('In-progress','Not-on-progress'),
)

class route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True)
    route = models.CharField(choices=ROUTE_PLAN, default='Unassigned',max_length=10)
    
    def __str__(self):
        return str(self.post)