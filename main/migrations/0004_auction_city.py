# Generated by Django 3.0.10 on 2020-10-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201001_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='city',
            field=models.CharField(default='', max_length=200, verbose_name='City'),
        ),
    ]
