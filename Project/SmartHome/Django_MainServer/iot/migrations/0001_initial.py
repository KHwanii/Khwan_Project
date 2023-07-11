# Generated by Django 4.1.7 on 2023-05-22 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CDS",
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
                ("place", models.CharField(max_length=50)),
                ("value", models.FloatField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="ControlCurtain",
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
                ("curtaincontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ControlDoorlock",
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
                ("doorlockcontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ControlHeater",
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
                ("control", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="DHT_humi",
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
                ("place", models.CharField(max_length=50)),
                ("value", models.FloatField()),
                ("created_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="DHT_temp",
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
                ("place", models.CharField(max_length=50)),
                ("value", models.FloatField()),
                ("created_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="ImageFile",
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
                ("file_name", models.CharField(max_length=80)),
                ("image_file", models.FileField(upload_to="image_file/%Y_%m_%d")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="SecFile",
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
                ("file_name", models.CharField(max_length=100)),
                ("sec_file", models.FileField(upload_to="sec_file/%Y_%m_%d")),
            ],
        ),
        migrations.CreateModel(
            name="Sensor",
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
                ("place", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("value", models.FloatField()),
                ("created_at", models.DateTimeField()),
            ],
        ),
    ]
