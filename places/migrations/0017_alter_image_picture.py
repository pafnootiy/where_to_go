# Generated by Django 4.0.9 on 2023-02-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_alter_image_position_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
