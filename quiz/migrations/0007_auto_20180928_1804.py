# Generated by Django 2.0.2 on 2018-09-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_answers_users_appeared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='users_appeared',
            field=models.CharField(default='', max_length=500),
        ),
    ]
