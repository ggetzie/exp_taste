# Generated by Django 3.0.10 on 2021-01-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210116_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='attempted',
            field=models.BooleanField(default=False, verbose_name='Collection attempted'),
        ),
    ]
