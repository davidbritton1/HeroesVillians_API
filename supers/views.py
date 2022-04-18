
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeroesVillianSerializer
from .models import HeroesVillians

@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        supers = HeroesVillians.objects.all()
        serializer = HeroesVillianSerializer(supers, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = HeroesVillianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(HeroesVillians, pk=pk)
    if request.method == 'GET':
        serializers = HeroesVillianSerializer(super);
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = HeroesVillianSerializer(super, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)