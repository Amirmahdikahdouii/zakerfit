# Generated by Django 4.2.2 on 2023-07-30 12:16

import Accounts.utils
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkOuts', '0002_dailyplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplan',
            name='date',
            field=Accounts.utils.ShamsiDateField(default=datetime.datetime(2023, 7, 30, 12, 16, 28, 61374, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='dailyplan',
            name='plan_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'FOR_TIME'), (2, 'AMRAP'), (3, 'EMOM'), (4, 'E2MOM'), (5, 'TABATA'), (6, 'OTHER')]),
        ),
        migrations.CreateModel(
            name='DailyPlanWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=400)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='WorkOuts.dailyplan')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_plan_workouts', to='WorkOuts.workout')),
            ],
        ),
    ]
