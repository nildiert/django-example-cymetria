from rest_framework import serializers

from .models import (
    OfficeInventory
)

class OfficeInventorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return OfficeInventory.objects.create(**validated_data)

