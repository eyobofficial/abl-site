# Generated by Django 2.0.6 on 2018-06-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20180609_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='widget',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', null=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='widget',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Record last modified date and time', null=True, verbose_name='Last Modified'),
        ),
    ]
