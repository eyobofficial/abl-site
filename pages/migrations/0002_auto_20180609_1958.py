# Generated by Django 2.0.6 on 2018-06-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last modified date and time', verbose_name='Last Modified')),
                ('title', models.CharField(max_length=255, verbose_name='Client name')),
                ('logo', models.ImageField(upload_to='clients/logo/')),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-featured'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last modified date and time', verbose_name='Last Modified')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'get_latest_by': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last modified date and time', verbose_name='Last Modified')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'get_latest_by': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last modified date and time', verbose_name='Last Modified')),
                ('client', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='testimonials/clients/')),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-featured', '-rating'],
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Record first created date and time', verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Record last modified date and time', verbose_name='Last Modified')),
                ('title', models.CharField(max_length=60)),
                ('sub_title', models.TextField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('link_title', models.CharField(max_length=60)),
                ('link_url', models.CharField(max_length=60)),
            ],
            options={
                'get_latest_by': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'get_latest_by': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='brand',
            name='service_description',
            field=models.TextField(blank=True, verbose_name='Service description'),
        ),
    ]
