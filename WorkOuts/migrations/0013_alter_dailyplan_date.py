# Generated by Django 4.2.2 on 2023-08-02 11:30

import Accounts.utils
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkOuts', '0012_alter_dailyplan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplan',
            name='date',
            field=Accounts.utils.ShamsiDateField(default=datetime.datetime(2023, 8, 2, 11, 30, 56, 494174, tzinfo=datetime.timezone.utc)),
        ),
    ]
