# Generated by Django 4.2.2 on 2023-07-10 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0004_coach_coach_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.PositiveSmallIntegerField(choices=[(1, 'instagram'), (2, 'twitter'), (3, 'telegram'), (4, 'facebook')])),
                ('url', models.URLField(max_length=1000)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coach.coach')),
            ],
        ),
    ]
