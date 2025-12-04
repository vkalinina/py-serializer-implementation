import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_str = json.dumps(serializer.data)
    return json_str.encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
