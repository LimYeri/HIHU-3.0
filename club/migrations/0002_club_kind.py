# Generated by Django 4.1.5 on 2023-01-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="kind",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
