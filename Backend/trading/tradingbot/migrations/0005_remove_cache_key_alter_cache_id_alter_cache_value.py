# Generated by Django 5.0.6 on 2024-05-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tradingbot", "0004_cache"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cache",
            name="key",
        ),
        migrations.AlterField(
            model_name="cache",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="cache",
            name="value",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
