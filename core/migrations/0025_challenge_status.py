# Generated by Django 3.1.7 on 2021-05-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_olimpimat_processed_descricao"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="status",
            field=models.CharField(
                blank=True, choices=[("A", "Aberto"), ("B", "Terminado")], max_length=2
            ),
        ),
    ]
