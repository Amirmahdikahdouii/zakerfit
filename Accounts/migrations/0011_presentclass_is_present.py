# Generated by Django 4.2.2 on 2023-07-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_alter_user_class_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentclass',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
    ]