# Generated by Django 2.2.3 on 2019-10-21 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20191020_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 11, 28, 16, 19350, tzinfo=utc)),
        ),
    ]
