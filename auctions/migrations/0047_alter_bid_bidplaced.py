# Generated by Django 3.2.9 on 2022-04-29 11:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0046_alter_bid_bidplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 11, 30, 34, 93797, tzinfo=utc)),
        ),
    ]
