# Generated by Django 4.2.2 on 2023-07-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_usertimepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertimepayment',
            name='sessions_remain',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
