# Generated by Django 4.2 on 2023-04-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_no',
            field=models.CharField(default='', max_length=30),
        ),
    ]
