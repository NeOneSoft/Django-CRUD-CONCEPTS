# Generated by Django 3.0.6 on 2020-05-24 23:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200523_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2020, 5, 24, 23, 20, 42, 820804, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
