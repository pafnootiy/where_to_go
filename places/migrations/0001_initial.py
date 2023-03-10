# Generated by Django 3.2.16 on 2023-01-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description_short', models.TextField(verbose_name='Описание короткое')),
                ('description_long', models.TextField(verbose_name='Описание полное')),
                ('latitude', models.FloatField(verbose_name='Долгота')),
                ('longitude', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
