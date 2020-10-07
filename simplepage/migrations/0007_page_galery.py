# Generated by Django 3.0.8 on 2020-09-30 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photogalery', '0002_remove_image_description'),
        ('simplepage', '0006_auto_20200924_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='galery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photogalery.Galery', verbose_name='Галерея изображений'),
        ),
    ]