# Generated by Django 5.1.6 on 2025-02-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_workerout_workeroutput"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="process",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="workeroutput",
            name="output_data",
            field=models.JSONField(),
        ),
    ]
