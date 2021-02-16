# Generated by Django 3.1.6 on 2021-02-16 16:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210216_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='role creation date', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(help_text='Name given to function / role / position', max_length=100, unique=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='role',
            name='value',
            field=models.IntegerField(help_text='Hierarchical value of function / role / position', verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, help_text='User address', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, help_text='Individual registration', max_length=15, unique=True, verbose_name='Individual registration'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='User registration date', verbose_name='data de registro'),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, help_text='brief description about the user', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_trusty',
            field=models.DateTimeField(blank=True, help_text='date the user was verified', null=True, verbose_name='is trusty'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, help_text="user's phone number", max_length=15, verbose_name='phone Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, help_text='user position / function / role', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='soft_delet',
            field=models.DateTimeField(blank=True, help_text='exclusion data the user if he has been excluded', null=True, verbose_name='deleted'),
        ),
    ]
