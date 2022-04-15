from rest_framework import serializers
from .models import HeroesVillians

class HeroesVillianSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroesVillians
        fields = ['name','alter_ego', 'primary_ability', 'secondary_ability','catchphrase', 'pk']