# Generated by Django 5.0.6 on 2024-05-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tradingbot", "0003_stockrecommendation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cache",
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
                ("key", models.CharField(max_length=255, unique=True)),
                ("value", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("expires_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]