# Generated by Django 3.0.8 on 2020-10-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0004_auto_20201015_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='email',
            field=models.EmailField(default='sp.raven@yandex.ru', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]