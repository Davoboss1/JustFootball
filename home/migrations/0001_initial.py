# Generated by Django 2.2 on 2019-04-16 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=45)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('Post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.football_posts')),
            ],
        ),
    ]
