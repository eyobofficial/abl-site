# Generated by Django 2.0.6 on 2018-06-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20180627_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]