# Generated by Django 5.1.2 on 2024-10-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0014_remove_subject_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='course_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
