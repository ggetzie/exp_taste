# Generated by Django 3.0.10 on 2020-10-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auction_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ['-end_date', 'id']},
        ),
        migrations.AddField(
            model_name='auctionlot',
            name='url',
            field=models.URLField(default='', max_length=2000, verbose_name='URL'),
        ),
    ]
