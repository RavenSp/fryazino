# Generated by Django 3.0.8 on 2020-09-25 04:07

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20200906_2223'),
        ('documents', '0016_auto_20200921_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='docsauthor',
            name='menu',
            field=mptt.fields.TreeOneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link_menu', to='menu.Menu', verbose_name='Пункт меню'),
        ),
    ]
