# Generated by Django 2.0.1 on 2018-04-27 05:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20180426_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menugroup',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('755bc71d-5a3f-4ff1-aa3c-ce809ea3b837'), unique=True),
        ),
    ]