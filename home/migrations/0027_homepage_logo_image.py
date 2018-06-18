# Generated by Django 2.0.4 on 2018-06-14 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0026_homepage_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='logo_image',
            field=models.ForeignKey(blank=True, help_text='Homepage logo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
