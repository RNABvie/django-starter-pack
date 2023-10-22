from django.contrib import admin
from djapp import models
# Register your models here.

admin.site.register(models.Worker)
admin.site.register(models.News)
admin.site.register(models.Rating)
admin.site.register(models.UserProfile)