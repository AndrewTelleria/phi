# Generated by Django 2.0.4 on 2018-07-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180711_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_text',
            field=models.CharField(help_text='Write an introduction for the business', max_length=255),
        ),
    ]
