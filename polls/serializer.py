from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'Protein', "Calories", "Fat",
                  "Fiber", "Carbs", "Salt", "Sugar")
