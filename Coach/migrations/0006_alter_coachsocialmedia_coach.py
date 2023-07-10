# Generated by Django 4.2.2 on 2023-07-10 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0005_coachsocialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachsocialmedia',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_medias', to='Coach.coach'),
        ),
    ]