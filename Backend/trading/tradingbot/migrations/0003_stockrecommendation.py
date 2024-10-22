# Generated by Django 5.0.6 on 2024-05-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tradingbot", "0002_remove_marketnews_id_alter_marketnews_news_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockRecommendation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("stock", models.CharField(max_length=100)),
                ("confidence", models.IntegerField()),
                ("advice", models.CharField(max_length=50)),
            ],
        ),
    ]
