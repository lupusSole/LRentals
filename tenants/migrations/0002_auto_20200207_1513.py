# Generated by Django 3.0.2 on 2020-02-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='movedIn',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
