# Generated by Django 4.2.14 on 2024-08-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_groupclass_options_styledescription_style_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupclass',
            name='description',
        ),
        migrations.RemoveField(
            model_name='groupclass',
            name='title',
        ),
        migrations.AddField(
            model_name='groupclass',
            name='description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.styledescription'),
        ),
        migrations.AddField(
            model_name='groupclass',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title', to='schedule.yogastyle'),
        ),
    ]
