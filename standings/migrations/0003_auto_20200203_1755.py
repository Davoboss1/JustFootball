# Generated by Django 2.2.1 on 2020-02-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0002_auto_20190417_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standings',
            options={'ordering': ['league_name', '-points'], 'verbose_name': 'Standing'},
        ),
    ]
