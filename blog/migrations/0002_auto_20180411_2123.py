# Generated by Django 2.0.4 on 2018-04-11 21:23

from django.db import migrations, models
import django.utils.timezone
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Post date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=models.CharField(max_length=250),
        ),
    ]
