# Generated by Django 5.1.4 on 2025-01-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon_user_app', '0008_customermodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='profile_pic',
            field=models.ImageField(default='user_profile/default.png', upload_to='user_profile/'),
        ),
    ]
