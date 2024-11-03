# Generated by Django 5.0.6 on 2024-07-21 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_photographer_photographerimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='ratings',
        ),
        migrations.AddField(
            model_name='photographer',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.CreateModel(
            name='CustomerRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('comment', models.TextField(blank=True, null=True)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='store.photographer')),
            ],
        ),
    ]