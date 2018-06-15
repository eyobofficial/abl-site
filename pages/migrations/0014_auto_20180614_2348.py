# Generated by Django 2.0.6 on 2018-06-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20180614_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Linkedin',
            field=models.URLField(blank=True, verbose_name='Linkedin link'),
        ),
        migrations.AddField(
            model_name='staff',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='staff',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitter link'),
        ),
    ]