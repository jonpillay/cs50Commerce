# Generated by Django 3.2.9 on 2022-01-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_itemlisting_highestbid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidItem',
        ),
        migrations.AddField(
            model_name='bid',
            name='bidItem',
            field=models.ManyToManyField(related_name='bids', to='auctions.ItemListing'),
        ),
    ]
