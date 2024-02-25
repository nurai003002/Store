# Generated by Django 5.0.2 on 2024-02-24 06:20

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('main_description', ckeditor.fields.RichTextField(verbose_name='Главное описание')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': '1) О нас ', 'verbose_name_plural': '1) О нас '},
        ),
        migrations.CreateModel(
            name='TeamInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_team/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_inline', to='secondary.team')),
            ],
            options={
                'unique_together': {('place_info', 'title')},
            },
        ),
    ]
