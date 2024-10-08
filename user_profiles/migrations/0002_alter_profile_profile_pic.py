# Generated by Django 4.2.14 on 2024-08-09 10:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='../static/images/default_profile_pic.jpg', max_length=255, verbose_name='image'),
        ),
    ]
