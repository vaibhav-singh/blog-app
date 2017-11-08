from django.shortcuts import render

# Create your views here.
from farm_api.models import Villages
from django.http.response import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``


def fetch_villages(request):
    latitude = request.GET['latitude']
    longitude = request.GET['longitude']
    # Villages.objects.create(
    #     name='Dg',
    #     coo = Point(12.4604, 43.9420)
    # )
    # q = Villages.objects.all()
    # print (dir(q[0]))
    villages_found = Villages.objects.filter(coo__distance_lte=(Point(latitude, longitude), D(km=2)))
    result = []
    for village in villages_found:
        result.append(dict(
            name=village.name,
            state=village.state,
            pincode=village.pincode,
            country=village.country,
            district=village.district
        ))
    return JsonResponse({
        'villages': result
    })

