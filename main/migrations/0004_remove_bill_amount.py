# Generated by Django 3.1 on 2021-07-05 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_bill_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='amount',
        ),
    ]
