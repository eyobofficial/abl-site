# Generated by Django 2.0.6 on 2018-06-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180609_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='quote',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='story',
            field=models.TextField(blank=True, verbose_name='Background story'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='what',
            field=models.TextField(blank=True, verbose_name='What we do'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='who',
            field=models.TextField(blank=True, verbose_name='Who we are'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(verbose_name='Testimonial'),
        ),
    ]
