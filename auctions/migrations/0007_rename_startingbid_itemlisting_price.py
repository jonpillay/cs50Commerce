# Generated by Django 3.2.9 on 2022-01-12 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_itemlisting_startingbid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemlisting',
            old_name='startingBid',
            new_name='price',
        ),
    ]
