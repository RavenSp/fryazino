# Generated by Django 3.0.8 on 2020-09-21 13:10

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20200906_2223'),
        ('news', '0002_category_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=mptt.fields.TreeOneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Menu', verbose_name='Пункт меню'),
        ),
    ]
