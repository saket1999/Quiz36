# Generated by Django 2.1.1 on 2018-09-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
