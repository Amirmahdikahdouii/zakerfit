# Generated by Django 4.2.2 on 2023-07-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0012_alter_grouponlineclasstime__class'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouponlineclass',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grouponlineclass',
            name='sessions_count',
            field=models.PositiveSmallIntegerField(default=12),
        ),
        migrations.AddField(
            model_name='grouponlineclass',
            name='sessions_count_in_week',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='grouponlineclass',
            name='sessions_duration',
            field=models.PositiveSmallIntegerField(default=60),
        ),
    ]
