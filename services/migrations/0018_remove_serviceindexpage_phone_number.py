# Generated by Django 2.0.4 on 2018-06-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20180619_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceindexpage',
            name='phone_number',
        ),
    ]
