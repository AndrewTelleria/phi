# Generated by Django 2.0.4 on 2018-05-03 23:42

from django.db import migrations
import django.utils.timezone
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='body',
            field=wagtail.core.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
