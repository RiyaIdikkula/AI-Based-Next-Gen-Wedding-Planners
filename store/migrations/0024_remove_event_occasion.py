# Generated by Django 5.0.6 on 2024-08-13 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_event_religion_starter_event_id_starter_package_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='occasion',
        ),
    ]
