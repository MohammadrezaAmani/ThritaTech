# Generated by Django 4.2.6 on 2023-10-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0003_remove_doctor_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="password",
            field=models.CharField(default="salam", max_length=100),
            preserve_default=False,
        ),
    ]
