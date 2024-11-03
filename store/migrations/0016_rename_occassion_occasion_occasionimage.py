# Generated by Django 5.0.6 on 2024-08-04 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_rename_user_email_passwordreset_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Occassion',
            new_name='Occasion',
        ),
        migrations.CreateModel(
            name='OccasionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='occasions_images/')),
                ('occasion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.occasion')),
            ],
        ),
    ]
