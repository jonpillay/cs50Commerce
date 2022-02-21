# Generated by Django 3.2.9 on 2022-02-08 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_auto_20220201_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlisting',
            name='winningBid',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wonItem', to='auctions.bid'),
        ),
    ]
