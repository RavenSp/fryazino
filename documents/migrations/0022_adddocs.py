# Generated by Django 3.0.8 on 2020-12-14 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0021_auto_20201019_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('doc', models.FileField(upload_to='uploads/%Y/%m/%d/documents', verbose_name='Документ')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Documents', verbose_name='Родительский документ')),
            ],
            options={
                'verbose_name': 'Дополнительный документ',
                'verbose_name_plural': 'Дополнительные документы',
            },
        ),
    ]