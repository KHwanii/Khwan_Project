# Generated by Django 4.1.7 on 2023-05-22 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("iot", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="controlheater",
            old_name="control",
            new_name="heatercontrol",
        ),
    ]
