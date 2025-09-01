from car.models import Car
from car.serializers import CarSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
