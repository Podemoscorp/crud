# Generated by Django 3.1.7 on 2021-04-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210408_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
