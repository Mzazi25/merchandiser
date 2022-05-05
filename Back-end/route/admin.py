from django.contrib import admin
from . models import User,Merchandiser,Manager
# Register your models here.

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Merchandiser)
