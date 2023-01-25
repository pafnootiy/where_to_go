from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404

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
            

        # print(context)

        return render(request, 'index.html', context)

def json_api(request,pk):

    id = get_object_or_404(Place, id=pk)
    locations = Place.objects.all()
    context = {}
    for location in locations:
        return HttpResponse (location.title)

