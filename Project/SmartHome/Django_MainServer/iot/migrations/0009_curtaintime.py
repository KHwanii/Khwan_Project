# Generated by Django 4.1.7 on 2023-05-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0008_rename_totalcontrol_totalsmartcontrol_total_control"),
    ]

    operations = [
        migrations.CreateModel(
            name="CurtainTime",
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
                ("time_day", models.DateTimeField()),
                ("time_night", models.DateTimeField()),
            ],
        ),
    ]
