from django.http import HttpResponse
from django.shortcuts import render
from Waterlize.utils import get_json
from . import models


def hello(request):
    return render(request, "firsttry.html")

def get_ajax_json(request):
    return HttpResponse(get_json())

def change_door(request):
    id = request.GET["id"]
    color = request.GET["color"]
    door = models.Doors.objects.get(id=id)
    if door is not None:
        door.color = color
        door.save()
    return HttpResponse("")

def change_temp(request):
    id = request.GET["id"]
    temp = request.GET["temp"]
    temperature = models.Temperature.objects.get(id=id)
    if temperature is not None:
        temperature.temp = temp
        temperature.save()
    return HttpResponse("")
