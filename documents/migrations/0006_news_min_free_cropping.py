# Generated by Django 3.0.8 on 2020-08-31 12:51

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_news_image_in_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='min_free_cropping',
            field=image_cropping.fields.ImageRatioField('image', '200x100', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='min free cropping'),
        ),
    ]
