# Generated by Django 3.2.9 on 2022-01-24 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_bid_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-bid']},
        ),
    ]
