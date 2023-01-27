# Generated by Django 3.2.16 on 2023-01-20 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_rename_image_image_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место'),
            preserve_default=False,
        ),
    ]