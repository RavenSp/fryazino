# Generated by Django 3.0.8 on 2020-08-31 09:46

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('documents', '0002_news_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='modifed',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='publisdDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='news',
            name='topNews',
            field=models.BooleanField(default=False, verbose_name='В главные новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documents.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='news',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Menu', verbose_name='Пункт меню'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст статьи'),
        ),
    ]
