# Generated by Django 3.1.7 on 2021-05-03 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_auto_20210502_2101"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="status",
            field=models.CharField(
                blank=True, choices=[("Aberto", "A"), ("Encerrado", "B")], max_length=50
            ),
        ),
    ]
