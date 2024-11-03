# Generated by Django 5.0.6 on 2024-08-06 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_starter_starterimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCourse',
            fields=[
                ('main_course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='main_courses/')),
                ('type', models.CharField(choices=[('veg', 'Vegetarian'), ('non-veg', 'Non-Vegetarian')], default='veg', max_length=10)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_courses', to='store.package')),
            ],
        ),
    ]
