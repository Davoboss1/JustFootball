# Generated by Django 2.2.1 on 2020-02-05 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200203_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='football_posts',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='football_posts',
            name='Date',
        ),
        migrations.AddField(
            model_name='football_posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
