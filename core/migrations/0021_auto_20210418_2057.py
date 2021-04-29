# Generated by Django 3.1.7 on 2021-04-18 23:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_auto_20210412_2034"),
    ]

    operations = [
        migrations.CreateModel(
            name="Olimpimat",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("descricao", models.TextField()),
                ("regulamento", models.FileField(upload_to="")),
                ("cronograma", models.FileField(upload_to="")),
                (
                    "criado_em",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.AddField(
            model_name="challenge",
            name="url_cadastro",
            field=models.URLField(default="ola.com"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challenge",
            name="url_prova",
            field=models.URLField(default="ola.com"),
            preserve_default=False,
        ),
    ]
