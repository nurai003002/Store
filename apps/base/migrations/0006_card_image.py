# Generated by Django 5.0.2 on 2024-02-23 06:17

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_card_alter_collection_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_on_card/', verbose_name='Фотография'),
        ),
    ]
