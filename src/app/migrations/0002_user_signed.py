# Generated by Django 5.0.1 on 2024-01-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]
