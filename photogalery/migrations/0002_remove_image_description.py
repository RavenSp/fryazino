# Generated by Django 3.0.8 on 2020-09-28 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogalery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
    ]
