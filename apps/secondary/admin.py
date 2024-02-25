from django.contrib import admin

from apps.secondary import models
# Register your models here.

admin.site.register(models.Team)
admin.site.register(models.Employee)
admin.site.register(models.About)
