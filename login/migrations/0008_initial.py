# Generated by Django 4.2 on 2023-04-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('confirm_password', models.CharField(blank=True, max_length=128, null=True)),
                ('mobile_no', models.BigIntegerField()),
            ],
        ),
    ]
