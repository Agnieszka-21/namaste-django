# Generated by Django 4.2.14 on 2024-10-02 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_remove_groupclass_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupclass',
            options={'ordering': ['first_class__week_day', 'start_time'], 'verbose_name_plural': 'group classes'},
        ),
    ]
