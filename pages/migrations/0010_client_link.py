# Generated by Django 2.0.6 on 2018-06-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_service_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='link',
            field=models.URLField(blank=True, verbose_name='Client webiste link'),
        ),
    ]