# Generated by Django 3.1.4 on 2020-12-31 00:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
