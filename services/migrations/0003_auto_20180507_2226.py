# Generated by Django 2.0.4 on 2018-05-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20180507_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='animal',
            field=models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog')], default='dog', max_length=1),
        ),
    ]