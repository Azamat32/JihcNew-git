# Generated by Django 3.1.3 on 2022-04-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20220427_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPostSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery', verbose_name='Картинки')),
                ('description', models.TextField(default='', max_length=100, verbose_name='Описание')),
                ('title', models.CharField(default='', max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Информация на главной странице',
            },
        ),
    ]
