# Generated by Django 2.0.4 on 2018-07-11 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='about',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
