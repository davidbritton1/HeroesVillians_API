# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer


@api_view(['GET', 'POST'])
def super_type_list(request):
    if request.method == 'GET':
        supers = SuperType.objects.all()
        serializer = SuperTypeSerializer(supers, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request, pk):
    super = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializers = SuperTypeSerializer(super);
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = SuperTypeSerializer(super, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)