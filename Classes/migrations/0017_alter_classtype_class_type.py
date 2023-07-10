# Generated by Django 4.2.2 on 2023-07-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0016_remove_time_class_name_time_class_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtype',
            name='class_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'PRESET_CLASS'), (2, 'GROUP_ONLINE_CLASS'), (3, 'PRIVATE_ONLINE_CLASS')], default=2),
        ),
    ]
