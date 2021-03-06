# Generated by Django 3.0.10 on 2021-01-24 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auctionlot_collected'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('source', models.URLField(default='', verbose_name='Source URL')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.AuctionLot')),
            ],
            options={
                'verbose_name': 'Lot Image',
                'verbose_name_plural': 'Lot Images',
                'db_table': 'lot_images',
            },
        ),
    ]
