# Generated by Django 4.2.3 on 2024-02-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0018_alter_event_eid"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="read",
            field=models.BooleanField(default=False),
        ),
    ]
