# Generated by Django 3.2.9 on 2022-05-10 10:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0056_alter_bid_bidplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 48, 59, 542451, tzinfo=utc)),
        ),
    ]