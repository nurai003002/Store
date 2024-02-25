from django.db import models

from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField
# Create your models here.


class About(models.Model):
    main_image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_about/',
        verbose_name='Главное Фото',
        blank =True, null=True
    )
    image1 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_about/',
        verbose_name='Фотография1',
        blank =True, null=True
    )
    image2 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_about/',
        verbose_name='Фотография2',
        blank =True, null=True
    )
    description = RichTextField(
        verbose_name = 'Описание'
    )
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = '1) О нас '
        verbose_name_plural = '1) О нас '

class Team(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name='фото'
    )
    main_description = RichTextField(
        verbose_name = 'Главное описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Команда'
        verbose_name_plural = '2) Команды'

class Employee(models.Model):
    image1 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'employee/',
        verbose_name='Фотография1',
        blank =True, null=True
    )
    image2 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'employee/',
        verbose_name='Фотография2',
        blank =True, null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='должность'
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name='опыт'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='адрес'
    )
    phone = models.CharField(
        verbose_name='номер телефона',
        max_length=255
    )
    email = models.EmailField(
        verbose_name='почта'
    )
    descriptions = RichTextField(
        verbose_name = 'описание'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '3) Cотрудник '
        verbose_name_plural = '3)  Сотрудники'