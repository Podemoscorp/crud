# Generated by Django 3.1.6 on 2021-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_post_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="new",
            name="views",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
