# Generated by Django 2.0.6 on 2018-07-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20180703_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='sent_date',
        ),
    ]
