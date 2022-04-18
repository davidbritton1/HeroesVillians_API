from rest_framework import serializers

from super_types.models import SuperType
from .models import HeroesVillians

class HeroesVillianSerializer(serializers.ModelSerializer, SuperType):
    class Meta:
        model = HeroesVillians
        fields = ['name','alter_ego', 'primary_ability', 'secondary_ability','catchphrase', SuperType]
        