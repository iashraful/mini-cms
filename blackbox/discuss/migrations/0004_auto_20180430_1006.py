# Generated by Django 2.0.1 on 2018-04-30 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_auto_20180430_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('77496f43-1d99-4a45-abac-fea22c47fa25'), editable=False),
        ),
    ]
