# Generated by Django 3.0.8 on 2020-09-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование галери')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание галери')),
                ('active', models.BooleanField(default=True, verbose_name='Актвиная галерея')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modifed', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название изображения')),
                ('description', models.TextField(verbose_name='Описание изображения')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/galery', verbose_name='Изображение')),
                ('galery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogalery.Galery', verbose_name='Галерея')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['id'],
            },
        ),
    ]