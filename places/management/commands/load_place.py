import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place


def add_place(url):
    response = requests.get(url)
    response.raise_for_status()
    response_for_object = response.json()

    place,created_place = Place.objects.get_or_create(
        title = response_for_object["title"],
        defaults={
            "short_description":response_for_object["description_short"],
            "long_description":response_for_object["description_long"],
            "longitude":response_for_object["coordinates"]['lng'],
            "latitude":response_for_object["coordinates"]['lat']
        }
    )

    if created_place:
        print(f'Добавлена локация {response_for_object["title"]}')
    else:
        print(f'Локация  {response_for_object["title"]} уже существует')
        return

    for picture_num,picture_url in enumerate(response_for_object["imgs"]):
        response = requests.get(picture_url)
        response.raise_for_status()

        picture = ContentFile(response.content)
        image,created_image = place.images.get_or_create(position=picture_num)

        if created_image:
            print(f'Добавляю фото {os.path.basename(picture_url)}')
            image.picture.save(os.path.basename(picture_url), picture, save=True)
        else:
            print(f'Фото {os.path.basename(picture_url)} уже существует')

 
class Command(BaseCommand):
    help = ' update locations'

    def add_arguments(self, parser):
        parser.add_argument("objects_url",nargs='+',type=str)          

    def handle(self, *args, **options):
        for objects_url in options["objects_url"]:

            if options['objects_url']:
                add_place(objects_url)






























# import os
# import requests
# from django.core.files.base import ContentFile
# from django.core.management.base import BaseCommand

# from places.models import Place



# def load_place(url):

#     response = requests.get(url)
#     response.raise_for_status()
#     places_response = response.json()
 

#     place,place_created = Place.objects.get_or_create(
#         places_response['title'],
#         defaults={'short_description': places_response['description_short'],
#                   'long_description': places_response['description_long'],
#                   'longitude': places_response['coordinates']['lng'],
#                   'latitude': places_response['coordinates']['lat'] }
#                   )

#     if place_created:
#         print(f'Добавляю место {places_response["title"]}')
#     else:
#         print(f'Место {places_response["title"]} уже добавлено')
#         return

#     for position, pic_url in enumerate(places_response['imgs']):
#         response = requests.get(pic_url)
#         response.raise_for_status()

#         img = ContentFile(response.content)

#         image_field, image_created = place.images.get_or_create(
#             position=position)
#         if image_created:
#             print(f'Добавляю фото {os.path.basename(pic_url)}')
#             image_field.img.save(os.path.basename(pic_url), img, save=True)
#         else:
#             print(f'Фото {os.path.basename(pic_url)} уже есть')

 


 
    
# class Command(BaseCommand):
#     help = "Loads place details into the database"

#     def add_arguments(self, parser):
#         parser.add_argument('object_url',nargs='+',type=str)

#     def handle(self, *args, **options):
#         for url in options['object_url']:
#             load_place(url)

            
 
# import os

# import requests
# from django.core.files.base import ContentFile
# from django.core.management.base import BaseCommand

# from places.models import Place


# def load_place(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     raw_place = response.json()

#     place, place_created = Place.objects.get_or_create(
#         title=raw_place['title'],
#         defaults={
#             'short_description': raw_place['description_short'],
#             'long_description': raw_place['description_long'],
#             'longitude': raw_place['coordinates']['lng'],
#             'latitude': raw_place['coordinates']['lat']},
#     )
 
    

#     if place_created:
#         print(f'Добавляю место {raw_place["title"]}')
#     else:
#         print(f'Место {raw_place["title"]} уже добавлено')
#         return
#     for position, pic_url in enumerate(raw_place['imgs']):
#         response = requests.get(pic_url)
#         response.raise_for_status()

#         img = ContentFile(response.content)

#         image_field, image_created = place.images.get_or_create(
#             position=position)
#         if image_created:
#             print(f'Добавляю фото {os.path.basename(pic_url)}')
#             image_field.img.save(os.path.basename(pic_url), img, save=True)
#         else:
#             print(f'Фото {os.path.basename(pic_url)} уже есть')


# class Command(BaseCommand):
#     help = "Loads place details into the database"

#     def add_arguments(self, parser):
#         parser.add_argument('place_url', nargs='+', type=str)

#     def handle(self, *args, **options):
#         for url in options['place_url']:
#             try:
#                 load_place(url)
#             except requests.exceptions.RequestException:
#                 print(f'\nВозникла ошибка с адресом {url} \n')
#                 continue