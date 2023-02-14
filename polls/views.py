from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from .serializer import FoodSerializer
# Create your views here.


@api_view(['GET'])
def getFood(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postFood(request):
    for obj in request.data:
        serializer = FoodSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)
