# Generated by Django 3.2.9 on 2022-01-13 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_itemlisting_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlisting',
            name='itemListedOn',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
