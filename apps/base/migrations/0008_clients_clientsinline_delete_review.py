# Generated by Django 5.0.2 on 2024-02-23 12:40

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_review'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='Review',
        ),
    ]
