# Generated by Django 2.0.2 on 2018-10-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20181015_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.TextField(default='aa', max_length=2000),
            preserve_default=False,
        ),
    ]