# Generated by Django 3.2.9 on 2022-04-29 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0049_auto_20220429_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 12, 0, 1, 820790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemlisting',
            name='auctionStart',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
