from django.contrib import admin
from .models import Merchandiser,Manager,Comment, Address

# Register your models here.
admin.site.register(Merchandiser)
admin.site.register(Manager)
admin.site.register(Address)