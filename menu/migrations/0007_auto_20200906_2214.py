# Generated by Django 3.0.8 on 2020-09-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200906_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallinks',
            name='weight',
            field=models.IntegerField(help_text='Вес определяет положение ссылки в выводе меню. Более легкие ссылки будут наверху', verbose_name='Вес ссылки'),
        ),
    ]