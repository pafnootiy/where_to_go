# Generated by Django 4.0.9 on 2023-02-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
