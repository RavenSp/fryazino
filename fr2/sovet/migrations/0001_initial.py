# Generated by Django 3.0.8 on 2020-09-06 21:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='okrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание округа')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округа',
            },
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название субъекта выдвижения')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Субъект выдвижения',
                'verbose_name_plural': 'Субъекты выдвижения',
            },
        ),
        migrations.CreateModel(
            name='deputat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uplaods/sovet', verbose_name='Фото депутата')),
                ('first_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('bDate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Биография депутата')),
                ('phones', models.CharField(blank=True, max_length=256, null=True, verbose_name='Контактные телефоны')),
                ('email', models.EmailField(default='sovet@fryazino.org', max_length=254, verbose_name='E-mail депутата')),
                ('grafic', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='График приёма')),
                ('chairman', models.BooleanField(default=False, help_text='Председателем может быть только один депутат.', verbose_name='Председатель Совета')),
                ('okrug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sovet.okrug', verbose_name='Округ')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sovet.party', verbose_name='Субъект выдвижения')),
            ],
            options={
                'verbose_name': 'Депутат',
                'verbose_name_plural': 'Депутаты',
            },
        ),
        migrations.CreateModel(
            name='commision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название комиссии')),
                ('description', models.TextField(verbose_name='Описание комисси')),
                ('slug', models.SlugField(max_length=255, verbose_name='URL')),
                ('tcom', models.CharField(choices=[('CM', 'Комиссия'), ('WG', 'Рабочая группа'), ('OT', 'Иное')], max_length=2, verbose_name='Тип комиссии')),
                ('chairman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sovet.deputat', verbose_name='Председатель комиссии')),
            ],
            options={
                'verbose_name': 'Комиссия',
                'verbose_name_plural': 'Комисии',
            },
        ),
    ]