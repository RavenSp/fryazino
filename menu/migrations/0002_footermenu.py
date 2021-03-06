# Generated by Django 3.0.8 on 2020-09-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='footerMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Пункт меню')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='URL')),
                ('active', models.BooleanField(default=True, verbose_name='Активная')),
                ('parrent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Menu', verbose_name='Ссылка на пункт главного меню')),
            ],
            options={
                'verbose_name': 'Пункт нижнего меню',
                'verbose_name_plural': 'Нижнее меню',
            },
        ),
    ]
