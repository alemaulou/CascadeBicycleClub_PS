# Generated by Django 3.0.6 on 2020-05-18 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renewal',
            name='phone_call_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 18, 22, 4, 0, 395179, tzinfo=utc), verbose_name='Phone Call Date'),
        ),
    ]
