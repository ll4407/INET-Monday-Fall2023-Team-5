# Generated by Django 4.2 on 2023-11-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_match"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="notification_sent",
            field=models.BooleanField(default=False),
        ),
    ]