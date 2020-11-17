# Generated by Django 3.0.8 on 2020-09-01 11:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('key', models.CharField(max_length=50, unique=True, verbose_name='Ключ блока')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст блока')),
            ],
            options={
                'verbose_name': 'Текстовый блок',
                'verbose_name_plural': 'Тестовые блоки',
            },
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]
