from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def get_serialized_json(location):
    images = location.images.all()
    serialized_json = {
        "title": location.title,
        "imgs": [img.picture.url for img in images],
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {
            "lng": location.longitude,
            "lat": location.latitude,
        }
    }

    return serialized_json


def convert_into_json(location):
    serialized_location = {"type": "Feature",
                           "geometry": {
                               "type": "Point",
                               "coordinates": [location.longitude, location.latitude]
                           },
                           "properties": {
                               "title": location.title,
                               "placeId": location.id,
                               "detailsUrl": reverse("location_info", kwargs={'pk': location.id})
                           }
                           }
                        
    return serialized_location



def json_api(request, pk):
    location = get_object_or_404(Place, id=pk)

    return JsonResponse(get_serialized_json(location), safe=False, json_dumps_params={
           'ensure_ascii': False, "indent": 2})


def index(request):
    locations = Place.objects.all()
    context = {}
    for location in locations:
        context['locations'] = { 
            "type": "FeatureCollection",
            "features": [convert_into_json(location) for location in locations]}
    return render(request, 'index.html', context)