# Generated by Django 3.0.8 on 2020-09-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bigbanner',
            old_name='URL',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='mbanner',
            old_name='URL',
            new_name='url',
        ),
    ]