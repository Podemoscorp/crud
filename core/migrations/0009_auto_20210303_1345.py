# Generated by Django 3.1.7 on 2021-03-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_auto_20210303_1121"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subject",
            old_name="nome",
            new_name="name",
        ),
    ]
