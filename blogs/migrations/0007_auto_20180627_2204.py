# Generated by Django 2.0.6 on 2018-06-27 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_post_read_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagory',
            options={'get_latest_by': ['-created_at', '-updated_at'], 'ordering': ['title'], 'verbose_name': 'Catagory', 'verbose_name_plural': 'Catagories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': ['-created_at'], 'ordering': ['-post', '-created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': ['-created_at'], 'ordering': ['-created_at', '-updated_at', 'title']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'get_latest_by': ['-created_at', '-updated_at'], 'ordering': ['title']},
        ),
    ]
