from rest_framework import serializers

from super_types.models import SuperType
from .models import HeroesVillian

class HeroesVillianSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroesVillian
        fields = ['name','alter_ego', 'primary_ability', 'secondary_ability','catchphrase']
