# Generated by Django 2.0.1 on 2018-04-11 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20180410_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='identifier',
            field=models.CharField(default=uuid.UUID('951c8b9e-335f-44bc-847f-d57cf770a78e'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='menugroup',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9ff48ac2-94d9-4702-89c2-51f60b2d3399'), unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(default='Hello', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='path',
            field=models.CharField(default=uuid.UUID('34631641-48d2-473b-8dc3-de13cd2bb21c'), max_length=64, unique=True),
        ),
    ]
