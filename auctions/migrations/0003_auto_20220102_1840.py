# Generated by Django 3.2.9 on 2022-01-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_itemlisting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemlisting',
            name='auctionEnd',
        ),
        migrations.RemoveField(
            model_name='itemlisting',
            name='auctionStart',
        ),
        migrations.RemoveField(
            model_name='itemlisting',
            name='currentBid',
        ),
        migrations.RemoveField(
            model_name='itemlisting',
            name='startingBid',
        ),
    ]
