# Generated by Django 2.2.1 on 2020-02-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='football_posts',
            options={'ordering': ['-Date']},
        ),
    ]