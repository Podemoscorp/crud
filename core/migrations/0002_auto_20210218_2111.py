# Generated by Django 3.1.6 on 2021-02-19 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="student",
            field=models.ForeignKey(
                help_text="enrollment student",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="poster",
            field=models.ForeignKey(
                help_text="post editor",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="new",
            name="poster",
            field=models.ForeignKey(
                help_text="news editor",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                help_text="Course teacher",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="course",
            field=models.ForeignKey(
                help_text="certificate course",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.course",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="referring_registration",
            field=models.ForeignKey(
                blank=True,
                help_text="Enrollment contained in the certificate",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.registration",
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="student",
            field=models.ForeignKey(
                help_text="student who will receive the certificate",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Alunos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="certificate",
            name="teacher",
            field=models.ForeignKey(
                help_text="teacher responsible for sending the certificate to the system / issuing the certificate",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Professor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
