# Generated by Django 3.0.8 on 2020-09-24 14:16

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('news', '0004_auto_20200922_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Темы'),
        ),
    ]
