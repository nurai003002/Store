# Generated by Django 5.0.2 on 2024-03-02 12:57

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_on_card/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': '5) Самое актуальное',
                'verbose_name_plural': '5) Самое октуальное',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_review/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': '6) Отзыв',
                'verbose_name_plural': '6) Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_collection/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': '3) Коллекция',
                'verbose_name_plural': '3) Коллекции',
            },
        ),
        migrations.CreateModel(
            name='NewArrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', ckeditor.fields.RichTextField(verbose_name='Главное Описание')),
                ('image', models.ImageField(upload_to='image_new_arrival/', verbose_name='Фото продукта')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': '4) Новое поступление',
                'verbose_name_plural': '4) Новые поступления',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=255, verbose_name='Главное название')),
                ('main_description', models.CharField(max_length=500, verbose_name='Главное описание')),
            ],
            options={
                'verbose_name': '7) Новость',
                'verbose_name_plural': '7) Новости',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo_image/', verbose_name='Логотип')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('facebook', models.URLField(verbose_name='Facebook URL')),
                ('twitter', models.URLField(verbose_name='Twitter URL')),
                ('instagram', models.URLField(verbose_name='Instagram URL')),
                ('schedule', ckeditor.fields.RichTextField(verbose_name='Расписание')),
                ('address', ckeditor.fields.RichTextField(verbose_name='Адрес')),
            ],
            options={
                'verbose_name': '1) Основная настройка',
                'verbose_name_plural': '1) Основные настройки',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_main/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': '2) Слайд ',
                'verbose_name_plural': '2) Слайды',
            },
        ),
        migrations.CreateModel(
            name='ClientsInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('review', models.TextField(verbose_name='Отзыв клиента')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients_words', to='base.clients')),
            ],
            options={
                'unique_together': {('place_info', 'name')},
            },
        ),
        migrations.CreateModel(
            name='NewsInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_news/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_inline', to='base.news')),
            ],
            options={
                'unique_together': {('place_info', 'title')},
            },
        ),
    ]
