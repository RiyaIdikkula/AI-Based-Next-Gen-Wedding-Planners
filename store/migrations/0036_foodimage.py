# Generated by Django 5.1.1 on 2024-10-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0035_remove_dress_image_dressimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="food_images/")),
                (
                    "predicted_food",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
    ]
