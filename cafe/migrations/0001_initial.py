# Generated by Django 4.1.5 on 2023-01-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cafe",
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
                ("name", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=300)),
                ("time", models.CharField(max_length=100)),
                (
                    "cafeImg",
                    models.ImageField(blank=True, null=True, upload_to="images/cafe"),
                ),
            ],
            options={
                "db_table": "cafes",
            },
        ),
    ]
