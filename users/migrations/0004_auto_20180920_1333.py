# Generated by Django 2.1.1 on 2018-09-20 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
