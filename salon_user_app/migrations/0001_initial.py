# Generated by Django 5.1.4 on 2024-12-20 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salon_admin_app', '0003_service_created_at_service_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='salon_admin_app.service')),
            ],
        ),
    ]
