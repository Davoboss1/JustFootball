# Generated by Django 3.0.3 on 2020-04-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images'),
        ),
    ]