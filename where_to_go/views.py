from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def get_serialized_json(location):
    # images = images.place.all()
    images = location.images.all()
    test = [img.picture.url for img in images] 
    print
    serialized_json= {
        "title":location.title,
        "imgs":[img.picture.url for img in images],
        "description_short":location.description_short,
        "description_long":location.description_long,
        "coordinates":{
            "lng":location.longitude,
            "lat":location.latitude,
        }
    }

    return serialized_json


# get_serialized_json()
def convert_in_json(location):
    serialized_location = {"type": "Feature",
                           "geometry": {
                               "type": "Point",
                               "coordinates": [location.latitude, location.longitude]
                           },
                           "properties": {
                               "title": location.title,
                               "detailsUrl": ""
                           }
                           }
    return serialized_location

def index(request):
    locations = Place.objects.all()
    context = {}
    for location in locations:

        context['places'] = {
            "type": "FeatureCollection",
            "features": [convert_in_json(location) for location in locations]}

        return render(request, 'index.html', context)

def json_api(request,pk):
    id = get_object_or_404(Place, id=pk)
    locations = Place.objects.all()
    context = {}
    for location in locations:
        return JsonResponse (get_serialized_json(location),safe=False,json_dumps_params={'ensure_ascii': False,"indent":2})

