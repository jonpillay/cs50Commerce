# Generated by Django 3.2.9 on 2022-04-07 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20220407_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=datetime.tzinfo),
        ),
    ]
