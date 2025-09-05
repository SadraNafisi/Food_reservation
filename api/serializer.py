from rest_framework import serializers
from reservation import models
class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemType
        fields=['name']
class ItemSerializer(serializers.ModelSerializer):
    type = ItemTypeSerializer(many=False)
    class Meta:
        model = models.Item
        exclude=('image','available',)

class SuborderSerializer(serializers.ModelSerializer):
    item=ItemSerializer(many=False)
    class Meta:
        model = models.SubOrder
        fields = '__all__'