# Generated by Django 5.0.6 on 2024-07-23 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_contactno_photographer_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('stylist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.package')),
            ],
        ),
        migrations.CreateModel(
            name='StylistImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='stylist_images/')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.stylist')),
            ],
        ),
    ]
