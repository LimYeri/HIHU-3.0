# Generated by Django 4.1.7 on 2023-03-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_alter_club_name_alter_club_number_alter_club_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='period',
            field=models.TextField(blank=True, null=True),
        ),
    ]
