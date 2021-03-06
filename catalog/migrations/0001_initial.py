# Generated by Django 3.0.8 on 2020-09-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0009_auto_20200906_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('menu', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Menu', verbose_name='Пункт меню')),
            ],
            options={
                'verbose_name': 'Тип муниципального учреждения',
                'verbose_name_plural': 'Типы муниципальных учреждений',
            },
        ),
        migrations.CreateModel(
            name='ListMUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Официальное полное название')),
                ('shortTitle', models.CharField(max_length=40, unique=True, verbose_name='Сокращенное назвение')),
                ('boss', models.CharField(max_length=512, verbose_name='ФИО руководителя')),
                ('bossPhone', models.CharField(help_text='Если телефонов несколько, введите их через запятую', max_length=20, verbose_name='Телефон руководителя')),
                ('zam', models.CharField(blank=True, max_length=512, null=True, verbose_name='ФИО заместителя руководителя')),
                ('zamPhone', models.CharField(blank=True, help_text='Если телефонов несколько, введите их через запятую', max_length=20, null=True, verbose_name='Телефон заместителя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание целей и задач учреждения')),
                ('postAddress', models.TextField(verbose_name='Почтовый адрес учреждения')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='E-mail учреждения')),
                ('fax', models.CharField(blank=True, max_length=150, null=True, verbose_name='Факс учреждения')),
                ('phone', models.CharField(help_text='Если телефонов несколько, введите их через запятую', max_length=256, verbose_name='Телефон учреждения')),
                ('type_mup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TypeMUP', verbose_name='Тип МУПа')),
            ],
            options={
                'verbose_name': 'Муниципальное учреждение',
                'verbose_name_plural': 'Муниципальные учреждения',
            },
        ),
    ]
