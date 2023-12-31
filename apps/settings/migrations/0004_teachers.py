# Generated by Django 4.2.8 on 2023-12-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0003_paket"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teachers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Имя Преподавателя"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="teachers/", verbose_name="Фото преподавателя"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Описание преподавателя"),
                ),
            ],
            options={
                "verbose_name": "Преподаватель",
                "verbose_name_plural": "Преподаватели",
            },
        ),
    ]
