# Generated by Django 4.2.3 on 2024-02-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0003_rename_question_contact_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(default="Nigeria", max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
