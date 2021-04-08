# Generated by Django 3.1.7 on 2021-04-08 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_auto_20210329_1802"),
    ]

    operations = [
        migrations.AddField(
            model_name="school",
            name="created",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                help_text="creation date",
                verbose_name="created in",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="classification",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
