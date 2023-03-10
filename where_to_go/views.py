from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def serialize_info_for_location(location):
    images = location.images.all()
    serialized_json = {
        'title': location.title,
        'imgs': [img.picture.url for img in images],
        'description_short': location.short_description,
        'description_long': location.long_description,
        'coordinates': {
            'lng': location.longitude,
            'lat': location.latitude,
        }
    }

    return serialized_json


def convert_location_to_geojson(location):
    serialized_location = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [location.longitude, location.latitude],
        },
        'properties': {
            'title': location.title,
            'detailsUrl': reverse(
                'location_info',
                kwargs={'pk': location.id},
            ),
        },
    }

    return serialized_location


def add_information_for_location(request, pk):
    location = get_object_or_404(Place, id=pk)

    return JsonResponse(
        serialize_info_for_location(location),
        json_dumps_params={'ensure_ascii': False},
    )


def index(request):
    locations = Place.objects.all()
    context = {
        'locations': {
            'type': 'FeatureCollection', 'features': [
                convert_location_to_geojson(location) for location in locations
            ]
        }
    }

    return render(request, 'index.html', context)
