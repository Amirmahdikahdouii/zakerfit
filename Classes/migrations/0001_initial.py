# Generated by Django 4.2.2 on 2023-07-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('place_count', models.PositiveSmallIntegerField()),
                ('athlete_count', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
