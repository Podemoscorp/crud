# Generated by Django 3.1.7 on 2021-04-12 23:18

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_challenge"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="criado_em",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="challenge",
            name="data_de_inicio",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challenge",
            name="data_de_termino",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challenge",
            name="descricao",
            field=models.TextField(
                default=datetime.datetime(2021, 4, 12, 23, 18, 25, 340996, tzinfo=utc)
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="challenge",
            name="nome",
            field=models.CharField(
                default=datetime.datetime(2021, 4, 12, 23, 18, 32, 165980, tzinfo=utc),
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]