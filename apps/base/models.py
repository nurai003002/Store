from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField

# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo_image/',
        verbose_name=  'Логотип'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    facebook = models.URLField(
        verbose_name = 'Facebook URL'
    )
    twitter = models.URLField(
        verbose_name = 'Twitter URL'
    )
    instagram = models.URLField(
        verbose_name = 'Instagram URL'
    )
    schedule = RichTextField(
        verbose_name = 'Расписание'
    )
    address = RichTextField(
        verbose_name = 'Адрес'
    )

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = '1) Основная настройка'
        verbose_name_plural = '1) Основные настройки'

class Slide(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = RichTextField(
        verbose_name = 'Описание'
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_main/',
        verbose_name='Фотография',
        blank =True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Слайд '
        verbose_name_plural = '2) Слайды'

class Collection(models.Model):
    main_description = RichTextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='image_collection/',
        verbose_name= 'Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    description = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.main_description
    
    class Meta:
        verbose_name = '3) Коллекция'
        verbose_name_plural = '3) Коллекции'

class NewArrival(models.Model):
    main_description = RichTextField(
        verbose_name = 'Главное Описание'
    )
    image = models.ImageField(
        upload_to='image_new_arrival/',
        verbose_name= 'Фото продукта'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '4) Новое поступление'
        verbose_name_plural = '4) Новые поступления'
    
class Card(models.Model):
    description = RichTextField(
        verbose_name = 'Описание'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена'
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_on_card/',
        verbose_name='Фотография',
        blank =True, null=True
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = '5) Самое актуальное'
        verbose_name_plural = '5) Самое октуальное'


class Clients(models.Model):         
    description = RichTextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='image_review/',
        verbose_name = 'Фотография'
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = '6) Отзыв'
        verbose_name_plural = '6) Отзывы'


class ClientsInline(models.Model):
    place_info = models.ForeignKey(Clients, related_name='clients_words' , on_delete=models.CASCADE)
    name  = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    review = models.TextField(
        verbose_name = 'Отзыв клиента'
    )

    class Meta:
        unique_together = ('place_info', 'name')


    
class News(models.Model):
    main_title = models.CharField(
        max_length = 255,
        verbose_name = 'Главное название'
    )
    main_description = models.CharField(
        max_length = 500,
        verbose_name = 'Главное описание'
    )
    def __str__(self):
        return self.main_title
    
    class Meta:
        verbose_name = '7) Новость'
        verbose_name_plural = '7) Новости'
    
class NewsInline(models.Model):
    place_info = models.ForeignKey(News, related_name='news_inline' , on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'image_news/',
        verbose_name='Фотография',
        blank =True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        verbose_name= 'Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank= True, null = True,
        verbose_name = "Время создания"
    )

    
    class Meta:
        unique_together = ('place_info', 'title')
    


