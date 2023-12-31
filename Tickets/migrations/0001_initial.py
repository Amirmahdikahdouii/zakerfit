# Generated by Django 4.2.2 on 2023-07-27 11:01

import Accounts.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Coach', '0009_coachability'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUsersQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(max_length=11, validators=[Accounts.utils.IranPhoneNumberValidator])),
                ('message', models.TextField()),
                ('date', Accounts.utils.ShamsiDateTimeField(auto_now_add=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('last_checked_date', Accounts.utils.ShamsiDateTimeField(auto_now=True)),
                ('is_answered', models.BooleanField(default=False)),
                ('answered_date', Accounts.utils.ShamsiDateTimeField(blank=True, null=True)),
                ('answered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anonymous_user_questions', to='Coach.coach')),
            ],
        ),
    ]
