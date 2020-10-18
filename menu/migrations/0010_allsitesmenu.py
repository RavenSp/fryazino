# Generated by Django 3.0.8 on 2020-10-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20200906_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='allSitesMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название сайта')),
                ('slug', models.SlugField(max_length=300, verbose_name='URL')),
                ('typeSite', models.CharField(choices=[('Органы власти', 'Вкладка органы власти'), ('Полезные ресурсы', 'Вкладка полезные ресурсы'), ('Информационные агенства', 'Вкладка информационные агенства'), ('Сайты муниципальных образований', 'Вкладка сайты муниципальных образований')], max_length=50, verbose_name='Тип сайта')),
                ('active', models.BooleanField(default=True, verbose_name='Активная')),
            ],
        ),
    ]
