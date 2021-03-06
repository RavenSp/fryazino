# Generated by Django 3.0.8 on 2020-09-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_auto_20200917_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documents',
            options={'ordering': ['-publishDate'], 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterField(
            model_name='doctype',
            name='title',
            field=models.CharField(help_text='Просьба, указывать значения в множественном числе', max_length=200, verbose_name='Тип документа'),
        ),
    ]
