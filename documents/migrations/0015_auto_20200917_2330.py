# Generated by Django 3.0.8 on 2020-09-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0014_auto_20200917_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
    ]