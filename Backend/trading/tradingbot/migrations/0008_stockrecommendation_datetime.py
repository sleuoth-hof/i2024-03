# Generated by Django 5.0.6 on 2024-07-02 16:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tradingbot", "0007_tradesignal_alter_csvfile_file_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="stockrecommendation",
            name="datetime",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
