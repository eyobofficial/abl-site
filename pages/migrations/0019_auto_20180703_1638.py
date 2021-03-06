# Generated by Django 2.0.6 on 2018-07-03 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'get_latest_by': ['-sent_date'], 'ordering': ['-sent_date', 'name']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='message',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
