# Generated by Django 4.2.2 on 2023-08-03 11:05

import Accounts.utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0006_alter_usertransaction_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userofflinepayment',
            name='payment_date',
            field=Accounts.utils.ShamsiDateField(blank=True, null=True),
        ),
    ]