# Generated by Django 4.2.2 on 2023-07-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0008_grouponlineclass_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouponlineclass',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
