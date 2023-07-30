# Generated by Django 4.2.2 on 2023-07-30 12:17

import Accounts.utils
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkOuts', '0003_alter_dailyplan_date_alter_dailyplan_plan_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplan',
            name='date',
            field=Accounts.utils.ShamsiDateField(default=datetime.datetime(2023, 7, 30, 12, 17, 45, 874040, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dailyplanworkout',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
