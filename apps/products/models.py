from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField
# Create your models here.

class Goods(models.Model):
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_goods/',
        verbose_name='Фотография',
        blank =True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    old_price = models.CharField(
        max_length = 255,
        verbose_name = 'Старая цена'
    )
    new_price = models.CharField(
        max_length = 255,
        verbose_name = 'Новая цена'
    )
    description = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '1) Товар'
        verbose_name_plural = '1) Товары'



class Cart(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Корзина'
        verbose_name_plural = '2) Корзина'


class Wishlist(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Избранные'
        verbose_name_plural = '2) Избранные'

