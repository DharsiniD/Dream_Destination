from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.TravellPlace)
admin.site.register(models.comments)
