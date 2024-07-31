from rest_framework import serializers
from .models import Ortable

class Orserializer(serializers.Serializer):
    class Meta:
        model=Ortable
        fields="__all__"