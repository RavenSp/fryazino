# Generated by Django 3.0.8 on 2020-09-01 13:09

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bigBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('URL', models.SlugField(verbose_name='URL')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('image', models.ImageField(upload_to='uploads/big-banners/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Большой баннер',
                'verbose_name_plural': 'Большие баннеры',
            },
        ),
        migrations.CreateModel(
            name='mBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('URL', models.SlugField(verbose_name='URL')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('image', models.ImageField(upload_to='uploads/m-banners/', verbose_name='Изображение')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '200x100', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка баннера')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры для карусели',
            },
        ),
    ]
