# Generated by Django 3.2.16 on 2023-01-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
