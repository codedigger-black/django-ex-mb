# Generated by Django 2.2.15 on 2020-10-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20201006_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='bceiduser',
            name='is_bcsc',
            field=models.BooleanField(default=False),
        ),
    ]