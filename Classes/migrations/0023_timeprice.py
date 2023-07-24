# Generated by Django 4.2.2 on 2023-07-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0022_alter_classtype_class_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('sessions_count', models.PositiveSmallIntegerField(default=12)),
            ],
        ),
    ]