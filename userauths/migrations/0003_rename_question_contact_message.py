# Generated by Django 4.2.3 on 2024-02-06 09:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0002_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="question",
            new_name="message",
        ),
    ]
