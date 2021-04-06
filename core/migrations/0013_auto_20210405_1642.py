# Generated by Django 3.1.7 on 2021-04-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_auto_20210405_1635"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                help_text="post cover image",
                upload_to="%Y/%m/%d/",
                verbose_name="Imagem",
            ),
        ),
    ]
