# Generated by Django 2.2.1 on 2020-02-05 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_auto_20200203_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores_date',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 8, 59, 43, 948085, tzinfo=utc), unique=True),
        ),
    ]
