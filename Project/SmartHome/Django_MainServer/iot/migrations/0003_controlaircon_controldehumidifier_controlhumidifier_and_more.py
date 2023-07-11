# Generated by Django 4.1.7 on 2023-05-22 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0002_rename_control_controlheater_heatercontrol"),
    ]

    operations = [
        migrations.CreateModel(
            name="ControlAircon",
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
                ("airconcontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ControlDehumidifier",
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
                ("dehumidifiercontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ControlHumidifier",
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
                ("humidefiercontrol", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name="sensor",
            name="category",
            field=models.CharField(max_length=80),
        ),
    ]
