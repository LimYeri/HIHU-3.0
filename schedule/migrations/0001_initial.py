# Generated by Django 4.1.5 on 2023-02-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
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
                ("startDate", models.DateTimeField()),
                ("endDate", models.DateTimeField()),
                ("event", models.CharField(max_length=300)),
            ],
            options={
                "db_table": "schedules",
            },
        ),
    ]
