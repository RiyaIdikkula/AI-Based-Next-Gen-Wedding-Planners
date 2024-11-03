# Generated by Django 5.0.6 on 2024-07-21 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_event_eventimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('photographer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.package')),
            ],
        ),
        migrations.CreateModel(
            name='PhotographerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photographer_images/')),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.photographer')),
            ],
        ),
    ]
