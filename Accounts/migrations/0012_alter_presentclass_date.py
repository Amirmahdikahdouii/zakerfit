# Generated by Django 4.2.2 on 2023-07-20 06:19

import Accounts.utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_presentclass_is_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentclass',
            name='date',
            field=Accounts.utils.ShamsiDateField(auto_now=True),
        ),
    ]
