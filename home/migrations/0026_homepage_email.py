# Generated by Django 2.0.4 on 2018-06-08 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20180607_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]