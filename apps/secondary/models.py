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
    main_description = RichTextField(
        verbose_name = 'Главное описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Команда'
        verbose_name_plural = '2) Команды'

class TeamInline(models.Model):
    place_info = models.ForeignKey(Team, related_name='team_inline', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_team/',
        verbose_name='Фото',
        blank =True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )

    class Meta:
        unique_together = ('place_info', 'title')
