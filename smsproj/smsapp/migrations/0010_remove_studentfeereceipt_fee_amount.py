# Generated by Django 5.1 on 2024-08-12 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0009_studentfeereceipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfeereceipt',
            name='fee_amount',
        ),
    ]
