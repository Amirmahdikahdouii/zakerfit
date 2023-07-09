# Generated by Django 4.2.2 on 2023-07-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0009_alter_grouponlineclass_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateClassBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='Classes.privateonlineclass')),
            ],
        ),
        migrations.CreateModel(
            name='GroupClassBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='Classes.grouponlineclass')),
            ],
        ),
    ]
