# Generated by Django 5.0.3 on 2024-04-29 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0004_alter_client_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='encryption_key',
            field=models.BinaryField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 13, 45, 18, 280346, tzinfo=datetime.timezone.utc)),
        ),
    ]
