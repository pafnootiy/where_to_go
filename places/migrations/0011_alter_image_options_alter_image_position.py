# Generated by Django 4.1.5 on 2023-01-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20230126_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, unique=True, verbose_name='Номер'),
        ),
    ]
