# Generated by Django 2.0.6 on 2018-06-30 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20180626_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Company Detail', 'verbose_name_plural': 'Company Details'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'Sliding Text', 'verbose_name_plural': 'Sliding Texts'},
        ),
        migrations.AlterModelOptions(
            name='widget',
            options={'verbose_name': 'Home Widget', 'verbose_name_plural': 'Home Widgets'},
        ),
    ]