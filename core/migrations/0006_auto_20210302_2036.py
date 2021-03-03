# Generated by Django 3.1.6 on 2021-03-02 23:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20210301_2143"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("nome", models.CharField(max_length=50)),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        help_text="Subject creation date",
                        verbose_name="created in",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="new",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="news cover image",
                upload_to="%Y/%m/%d/",
                verbose_name="Imagem",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=stdimage.models.StdImageField(
                help_text="post cover image",
                upload_to="%Y/%m/%d/",
                verbose_name="Imagem",
            ),
        ),
        migrations.CreateModel(
            name="SubjectPost",
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
                (
                    "created_in",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.post"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.subject"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubjectNew",
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
                (
                    "created_in",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "new",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.new"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.subject"
                    ),
                ),
            ],
        ),
    ]