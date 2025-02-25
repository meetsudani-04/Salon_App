# Generated by Django 5.1.4 on 2025-01-08 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon_user_app', '0012_appointmentbookmodel_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon_user_app.customermodel')),
            ],
        ),
    ]
