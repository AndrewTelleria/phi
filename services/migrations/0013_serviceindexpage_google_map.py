# Generated by Django 2.0.4 on 2018-06-08 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20180607_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceindexpage',
            name='google_map',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]