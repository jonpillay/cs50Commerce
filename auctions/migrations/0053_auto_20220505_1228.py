# Generated by Django 3.2.9 on 2022-05-05 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0052_alter_bid_bidplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 28, 12, 367801, tzinfo=utc)),
        ),
    ]
