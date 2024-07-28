from rest_framework.decorators import api_view
from rest_framework.response import Response
from reservation.models import Item , SubOrder
from .serializer import *
@api_view(['GET'])
def getRoute(request):
    routes=[
        {'GET':'order-list-all/'},
        {'GET':'order-list/'},
    ]
    return Response(routes)
@api_view(['GET'])
def getItem(request):
    items = Item.objects.all()

    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
@api_view(['GET'])
def getSuborder(request):
    suborders = SubOrder.objects.all()

    serializers = SuborderSerializer(suborders, many=True)
    return Response(serializers.data)