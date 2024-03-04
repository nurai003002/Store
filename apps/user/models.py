from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'Пользеватель'
        verbose_name_plural = 'Пользаватели'