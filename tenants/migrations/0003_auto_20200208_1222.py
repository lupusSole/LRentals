# Generated by Django 3.0.2 on 2020-02-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_auto_20200207_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='profileCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
