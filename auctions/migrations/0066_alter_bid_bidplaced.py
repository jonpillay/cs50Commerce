# Generated by Django 3.2.9 on 2022-09-06 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0065_auto_20220906_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidPlaced',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
