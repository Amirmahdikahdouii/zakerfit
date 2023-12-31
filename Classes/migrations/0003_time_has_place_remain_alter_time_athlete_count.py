# Generated by Django 4.2.2 on 2023-07-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0002_alter_time_athlete_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='has_place_remain',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='athlete_count',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
