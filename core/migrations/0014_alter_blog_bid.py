# Generated by Django 4.2.3 on 2024-02-09 20:53

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_alter_blog_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="bid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=10,
                max_length=30,
                prefix="",
                unique=True,
            ),
        ),
    ]
