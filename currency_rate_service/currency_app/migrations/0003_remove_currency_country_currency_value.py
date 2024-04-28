# Generated by Django 4.2.11 on 2024-04-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0002_rename_blogpost_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='country',
        ),
        migrations.AddField(
            model_name='currency',
            name='value',
            field=models.CharField(default='0.0', max_length=10),
        ),
    ]