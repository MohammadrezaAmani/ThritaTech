# Generated by Django 4.2.6 on 2023-10-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercise", "0004_organ_target_exercise_keywords_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="organ",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
