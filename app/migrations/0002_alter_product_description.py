# Generated by Django 5.0.4 on 2024-04-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
