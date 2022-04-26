from django.contrib import admin
from .models import Merchandiser,Manager,Route,Comment

# Register your models here.
admin.site.register(Merchandiser)
admin.site.register(Manager)
admin.site.register(Route)
admin.site.register(Comment)