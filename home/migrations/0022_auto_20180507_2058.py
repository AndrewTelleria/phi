# Generated by Django 2.0.4 on 2018-05-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20180507_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='job_title',
            field=models.CharField(max_length=254, verbose_name='Job title'),
        ),
        migrations.AlterField(
            model_name='people',
            name='last_name',
            field=models.CharField(max_length=254, verbose_name='Last name'),
        ),
    ]
