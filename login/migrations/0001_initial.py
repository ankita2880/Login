# Generated by Django 4.1.7 on 2023-04-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="login",
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
                ("Email", models.EmailField(max_length=100)),
                ("Password", models.CharField(max_length=20)),
            ],
        ),
    ]
