from Waterlize.models import Temperature, Doors
import json


def get_json():
    dict_result = {"temp": {}, "doors": {}}
    colors = ["red", "green", "gray"]

    for temp in Temperature.objects.all():
        dict_result["temp"][temp.id] = temp.temp

    for door in Doors.objects.all():
        dict_result["doors"][door.id] = door.color if door.color in colors else "gray"

    return json.dumps(dict_result)
