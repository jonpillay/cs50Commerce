# Generated by Django 3.2.9 on 2022-08-23 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0058_auto_20220510_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 11, 14, 22, 270291, tzinfo=utc)),
        ),
    ]
