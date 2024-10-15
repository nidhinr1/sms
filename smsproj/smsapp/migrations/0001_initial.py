# Generated by Django 5.1 on 2024-08-08 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('scholarship', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('admission_date', models.DateField()),
                ('admission_number', models.CharField(max_length=6, unique=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.course')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.studentdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.studentdetails')),
            ],
        ),
    ]