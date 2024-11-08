# Generated by Django 5.1.1 on 2024-10-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_foodimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('guest_count', models.PositiveIntegerField()),
                ('venue_type', models.CharField(choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('destination', 'Destination')], max_length=20)),
                ('preferred_colors', models.CharField(max_length=100)),
                ('season', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], max_length=10)),
            ],
        ),
    ]
