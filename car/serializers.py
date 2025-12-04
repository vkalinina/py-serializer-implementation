from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(required=True, max_length=64)
    manufacturer = serializers.CharField(required=True, max_length=64)
    horse_power = serializers.IntegerField(
        min_value=1, max_value=1914
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
