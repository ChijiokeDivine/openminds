# Generated by Django 4.2.3 on 2024-01-30 16:01

import ckeditor_uploader.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                        prefix="blog-",
                        unique=True,
                    ),
                ),
                ("blog_title", models.CharField(default="Barbify", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="blog-img.jpg",
                        upload_to=core.models.user_directory_path,
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        default="blog-cover.jpg",
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
                ("featured", models.BooleanField(default=False)),
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
        migrations.CreateModel(
            name="wishlist",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "blog",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.blog",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "wishlists",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("occupation", models.CharField(max_length=40)),
                ("title", models.CharField(max_length=50)),
                ("review", models.CharField(max_length=130)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Reviews",
            },
        ),
        migrations.CreateModel(
            name="BlogImages",
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
                    "images",
                    models.ImageField(default="blog-img.jpg", upload_to="blog-images"),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "blog",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_images",
                        to="core.blog",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Blogs images",
            },
        ),
    ]