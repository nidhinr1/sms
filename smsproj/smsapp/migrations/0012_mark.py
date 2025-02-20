# Generated by Django 5.1.2 on 2024-10-15 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0011_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marks_obtained', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.studentdetails', to_field='admission_number')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.subject')),
            ],
        ),
    ]
