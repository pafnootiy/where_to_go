import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


def add_place(url):
    response = requests.get(url)
    response.raise_for_status()
    response_for_object = response.json()

    place, created_place = Place.objects.get_or_create(
        title=response_for_object['title'],
        defaults={
            'short_description': response_for_object['description_short'],
            'long_description': response_for_object['description_long'],
            'longitude': response_for_object['coordinates']['lng'],
            'latitude': response_for_object['coordinates']['lat']
        }
    )

    if created_place:
        print(f"Добавлена локация {response_for_object['title']}")
    else:
        print(f"Локация  {response_for_object['title']} уже существует")
        return

    for picture_num, picture_url in enumerate(response_for_object['imgs']):
        response = requests.get(picture_url)
        response.raise_for_status()

        picture = ContentFile(response.content)
        image, created_image = place.images.get_or_create(position=picture_num)

        if created_image:
            print(f'Добавляю фото {os.path.basename(picture_url)}')
            image.picture.save(
                os.path.basename(picture_url), picture, save=True
            )
        else:
            print(f'Фото {os.path.basename(picture_url)} уже существует')


class Command(BaseCommand):
    help = ' update locations'

    def add_arguments(self, parser):
        parser.add_argument('objects_url', nargs='+', type=str)

    def handle(self, *args, **options):
        for objects_url in options['objects_url']:

            if options['objects_url']:
                add_place(objects_url)
