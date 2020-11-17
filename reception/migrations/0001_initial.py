# Generated by Django 3.0.8 on 2020-10-12 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Получатель')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Получатель обращения',
                'verbose_name_plural': 'Получатели обращений',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название темы')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail рассылки')),
            ],
            options={
                'verbose_name': 'Тема обращения',
                'verbose_name_plural': 'Темы обращения',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='apperal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
                ('post_address', models.CharField(max_length=500, verbose_name='Почтовый адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('file', models.FileField(blank=True, upload_to='reception/%Y/%m/%d/', verbose_name='Приложенный файл')),
                ('personal', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления обращения')),
                ('ipaddres', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.theme', verbose_name='Тема обращения')),
            ],
            options={
                'verbose_name': 'Обращение гражданина',
                'verbose_name_plural': 'Обращения граждан',
                'ordering': ['-created'],
            },
        ),
    ]
