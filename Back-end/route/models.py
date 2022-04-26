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
