# Generated by Django 5.0.6 on 2024-05-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tradingbot", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marketnews",
            name="id",
        ),
        migrations.AlterField(
            model_name="marketnews",
            name="news_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
