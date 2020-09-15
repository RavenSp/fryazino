# Generated by Django 3.0.8 on 2020-09-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_sociallinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinks',
            name='weight',
            field=models.IntegerField(default=1, help_text='Вес определяет положение ссылки в выводе меню. Более легкие ссылки будут наверху', unique=False, verbose_name='Вес ссылки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='footermenu',
            name='weight',
            field=models.IntegerField(help_text='Вес определяет положение ссылки в выводе меню. Более легкие ссылки будут наверху', unique=False, verbose_name='Вес ссылки'),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='linkClass',
            field=models.CharField(help_text='Классы можно искать на сайте <a href="https://fontawesome.ru/all-icons/" target="_blank">https://fontawesome.ru/all-icons/</a>', max_length=50, verbose_name='Класс значка fontawesome'),
        ),
    ]
