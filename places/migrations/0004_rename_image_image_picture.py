# Generated by Django 3.2.16 on 2023-01-20 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20230121_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='picture',
        ),
    ]
