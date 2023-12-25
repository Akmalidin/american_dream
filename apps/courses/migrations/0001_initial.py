# Generated by Django 4.2.8 on 2023-12-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                    "image",
                    models.ImageField(upload_to="courses/", verbose_name="Фото курса"),
                ),
                (
                    "course_name",
                    models.CharField(max_length=20, verbose_name="Название курса"),
                ),
                ("course_description", models.TextField(verbose_name="Описание курса")),
                (
                    "time",
                    models.IntegerField(
                        help_text="В месяцах: 12", verbose_name="Длительность курса"
                    ),
                ),
                ("course_price", models.IntegerField(verbose_name="Цена курса")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
