# Generated by Django 3.1.7 on 2021-04-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_auto_20210412_2018"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="descricao",
            field=models.TextField(blank=True),
        ),
    ]