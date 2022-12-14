# Generated by Django 3.2.9 on 2022-05-10 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0057_alter_bid_bidplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlisting',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 13, 43, 54, 55035, tzinfo=utc)),
        ),
    ]
