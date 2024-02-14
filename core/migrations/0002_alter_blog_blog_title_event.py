# Generated by Django 4.2.3 on 2024-02-02 20:10

import ckeditor_uploader.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_title",
            field=models.CharField(default="blog", max_length=100),
        ),
        migrations.CreateModel(
            name="Event",
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
                (
                    "bid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh12345",
                        length=10,
                        max_length=20,
                        prefix="event-",
                        unique=True,
                    ),
                ),
                ("event_title", models.CharField(default="event", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="event-img.jpg",
                        upload_to=core.models.user_directory_path,
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        default="event-cover.jpg",
                        upload_to=core.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, default="Case study ", null=True
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                ("start_date", models.TimeField(blank=True, null=True)),
                ("end_date", models.TimeField(blank=True, null=True)),
                ("venue_date", models.DateField(blank=True, null=True)),
                ("venue", models.CharField(default="event venue", max_length=100)),
                ("featured", models.BooleanField(default=False)),
                ("host", models.CharField(default="event venue", max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]