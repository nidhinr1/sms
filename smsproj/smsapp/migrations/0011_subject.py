# Generated by Django 5.1.2 on 2024-10-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0010_remove_studentfeereceipt_fee_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=20)),
                ('semester', models.IntegerField()),
            ],
        ),
    ]
