# Generated by Django 4.2.14 on 2024-08-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0022_groupclass_teacher_bio_alter_groupclass_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groupclass',
            name='first_class',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
