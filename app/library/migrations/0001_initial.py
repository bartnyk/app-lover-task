# Generated by Django 5.1.1 on 2024-09-09 23:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "serial_number",
                    models.PositiveIntegerField(
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{6}$",
                                "Library card number must be exactly 6 digits.",
                            )
                        ],
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Rent",
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
                ("rent_date", models.DateTimeField(auto_now_add=True)),
                (
                    "library_card_number",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{6}$",
                                "Library card number must be exactly 6 digits.",
                            )
                        ],
                    ),
                ),
                ("return_date", models.DateTimeField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library.book"
                    ),
                ),
            ],
        ),
    ]
