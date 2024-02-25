from django.contrib import admin

from apps.products import models

# Register your models here.

admin.site.register(models.Goods)
admin.site.register(models.Cart)
admin.site.register(models.Wishlist)

