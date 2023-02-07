# Generated by Django 4.0.9 on 2023-02-07 03:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание полное'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание короткое'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=95, verbose_name='Заголовок'),
        ),
    ]
