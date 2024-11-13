from rest_framework import serializers
from reservation import models
class Food_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food_Type
        fields=['name']
class ItemSerializer(serializers.ModelSerializer):
    type = Food_TypeSerializer(many=False)
    class Meta:
        model = models.Item
        exclude=('image','available',)

class SuborderSerializer(serializers.ModelSerializer):
    item=ItemSerializer(many=False)
    class Meta:
        model = models.SubOrder
        fields = '__all__'