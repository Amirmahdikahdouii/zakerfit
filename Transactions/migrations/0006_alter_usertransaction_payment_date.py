# Generated by Django 4.2.2 on 2023-08-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0005_alter_usertransaction_last_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
