# Generated by Django 3.2.8 on 2022-10-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
