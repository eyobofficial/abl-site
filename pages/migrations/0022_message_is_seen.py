# Generated by Django 2.0.6 on 2018-07-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20180703_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_seen',
            field=models.BooleanField(default=False, verbose_name='Seen'),
        ),
    ]
