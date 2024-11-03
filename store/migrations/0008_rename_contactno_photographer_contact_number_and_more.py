# Generated by Django 5.0.6 on 2024-07-23 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_photographer_ratings_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photographer',
            old_name='contactno',
            new_name='contact_number',
        ),
        migrations.RemoveField(
            model_name='photographer',
            name='average_rating',
        ),
        migrations.DeleteModel(
            name='CustomerRating',
        ),
    ]
