# Generated by Django 4.2.6 on 2023-10-19 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0003_remove_doctor_user"),
        ("exercise", "0002_remove_exercise_others_exercise_accessories_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Displacement",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Goal",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="PlacementPosition",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name="exercise",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="doctor.doctor",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exercise",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="exercise",
            name="target",
            field=models.TextField(blank=True, null=True),
        ),
    ]