# Generated by Django 2.0.4 on 2018-06-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20180607_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='display_price',
            field=models.CharField(help_text='Ex. $50/day', max_length=255),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='50.00', max_digits=6),
        ),
    ]
