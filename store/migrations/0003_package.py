# Generated by Django 5.0.6 on 2024-07-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
