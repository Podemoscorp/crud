# Generated by Django 3.1.6 on 2021-02-15 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210215_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='criado_em',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='curso',
            name='criado_em',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='postado_em',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
