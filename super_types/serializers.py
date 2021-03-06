from pyexpat import model
from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer, SuperType):
    class Meta:
        model = SuperType
        fields = ['type']